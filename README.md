# README.md

# Whisper Speech-to-Text UI

This is a graphical user interface (GUI) for converting speech to text using OpenAI's Whisper model. The application is built using PyQt5 and the `transformers` library from Hugging Face.

## Features
- Upload audio files or record audio directly using your laptop's microphone.
- Automatically detect the language of the audio.
- Supports multiple output formats: `.txt`, `.json`, `.csv`, `.rtf`, `.docx`.
- Responsive, minimal, and modern UI with real-time transcription progress.
- Error handling for unsupported audio devices and file operations.

## Requirements
- Python 3.7+
- PyQt5
- torch
- transformers

## Installation

Clone the repository and install the required packages:

```sh
git clone https://github.com/username/whisper_ui_project.git
cd whisper_ui_project
pip install -r requirements.txt
```

## Running the Application

To run the application, simply execute the following command:

```sh
python whisper_ui_app.py
```

## Usage
1. Open the application by running `whisper_ui_app.py`.
2. You can either upload an audio file or record your audio using the provided buttons.
3. Select the output format you wish to save the transcription in.
4. Click "Start Transcription" to transcribe the audio into text.
5. Choose the location to save the output file.

## Project Structure
- `whisper_ui_app.py`: Main application code.
- `recorded_audio/`: Directory to store recorded audio files.
- `assets/`: Contains icons and styles for the UI.
- `requirements.txt`: Lists all dependencies required to run the project.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contribution
Feel free to fork this repository and contribute by submitting pull requests. For major changes, please open an issue first to discuss what you would like to change.

## Contact
If you have any questions or issues, please feel free to contact me at `your-email@example.com`.

---

# LICENSE

MIT License

Copyright (c) 2024 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

