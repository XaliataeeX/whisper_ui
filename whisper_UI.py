import sys
import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog, QComboBox, QProgressBar, QTextEdit
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt
import os

# Device configuration
device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

# Load model and processor
model_id = "openai/whisper-large-v3-turbo"
try:
    model = AutoModelForSpeechSeq2Seq.from_pretrained(
        model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
    ).to(device)
    processor = AutoProcessor.from_pretrained(model_id)
except Exception as e:
    print(f"Error loading model: {e}")
    sys.exit(1)

pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    torch_dtype=torch_dtype,
    device=device,
    return_timestamps=True
)

class WhisperApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Whisper Speech-to-Text")
        self.setGeometry(100, 100, 600, 400)
        self.setMinimumSize(400, 300)

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(245, 245, 245))
        palette.setColor(QPalette.WindowText, Qt.black)
        self.setPalette(palette)

        # Audio Input Selection
        file_button = QPushButton("Upload Audio File")
        file_button.clicked.connect(self.load_audio_file)
        main_layout.addWidget(file_button)

        # Output Format Selection
        self.format_box = QComboBox()
        self.format_box.addItems([".txt", ".json", ".csv", ".rtf", ".docx"])
        main_layout.addWidget(QLabel("Select Output Format:"))
        main_layout.addWidget(self.format_box)

        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        main_layout.addWidget(self.progress_bar)

        # Start Processing Button
        process_button = QPushButton("Start Transcription")
        process_button.clicked.connect(self.process_audio)
        main_layout.addWidget(process_button)

        # Transcription Output Preview
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        main_layout.addWidget(self.output_text)

    def load_audio_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Audio File", "", "Audio Files (*.mp3 *.wav)")
        if file_name:
            self.audio_file_path = file_name
            self.output_text.append(f"Audio file loaded: {os.path.basename(file_name)}")

    def process_audio(self):
        if not hasattr(self, 'audio_file_path'):
            self.output_text.append("No audio file selected. Please upload an audio file.")
            return

        self.progress_bar.setValue(10)
        self.output_text.append("Processing audio...")
        try:
            result = pipe(self.audio_file_path)
            self.progress_bar.setValue(90)
            self.output_text.append(result['text'])
            self.save_transcription(result['text'])
            self.progress_bar.setValue(100)
        except Exception as e:
            self.output_text.append(f"Error during transcription: {e}")
            self.progress_bar.setValue(0)

    def save_transcription(self, transcription):
        save_path, _ = QFileDialog.getSaveFileName(self, "Save Transcription", f"transcription{self.format_box.currentText()}", f"*{self.format_box.currentText()}")
        if save_path:
            try:
                with open(save_path, 'w') as file:
                    file.write(transcription)
                self.output_text.append(f"Transcription saved as {save_path}")
            except Exception as e:
                self.output_text.append(f"Error saving transcription: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WhisperApp()
    ex.show()
    sys.exit(app.exec_())