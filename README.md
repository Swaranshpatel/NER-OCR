# OCR and NER Application

This application utilizes Optical Character Recognition (OCR) and Named Entity Recognition (NER) to extract text and named entities from images and PDFs.

## Features

- Extract text from images and PDFs using OCR.
- Recognize named entities in text using NER.
- Save extracted text and named entities to Word documents.

## Prerequisites

- Python 3.12.2
- Install the required libraries listed in `requirements.txt`.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up Tesseract OCR:
   - Install Tesseract OCR and update the path in `config.py`.

## Usage

1. Run `main.py`:
   ```
   python main.py
   ```
2. Open the application in your web browser (by default, it should be available at `http://localhost:5000`).

## Endpoints

- `/extract_entities`: Extract named entities from provided text.
- `/extract_text`: Extract text from images or PDFs.

## File Structure

- `main.py`: Flask application with endpoints for text and entity extraction.
- `OCR.py`: Module for OCR functionality.
- `NER.py`: Module for NER functionality.
- `config.py`: Configuration file for paths and settings. make sure you added your teserect-ocr path eg. "C:\Program Files\Tesseract-OCR or C:\Program Files (x86)\Tesseract-OCR" if you dont have one please install
- `requirements.txt`: List of Python dependencies.

## Credits

- OCR functionality [pytesseract](https://github.com/madmaze/pytesseract).
- NER functionality using 'xlm-roberta-large-finetuned-conll03-english' model .

