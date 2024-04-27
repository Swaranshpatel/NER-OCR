'''
PYTHON 3.12.2
'''

from OCR import ocr
from NER import ner_tagger
from flask import Flask, request, jsonify, render_template
from PIL import Image
import tempfile
import os
import config 

app = Flask(__name__)

ner = ner_tagger()
ocr_tool = ocr()
output_path = config.OUTPUT_FILE_PATH

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/extract_entities', methods=['POST'])
def extract_entities():
    try:
        text = request.form['text']
        entities = ner.ner_extraction(text)
        if entities:
            ner.save_to_docx(entities, output_path)
            ent = [(e['entity'],e['word']) for e in entities if e['score'] > 0.5]
            return jsonify({"message": "Named entities extracted and saved successfully!", "entities": '\n'.join([str((k,v)) for k,v in ner.decode_ner(ent).items()])}), 200
        else:
            return jsonify({"error": "Failed to extract named entities."}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/extract_text', methods=['POST'])
def extract_text():
    try:
        if 'image' in request.files:
            image = request.files['image']
            image = Image.open(image)
            text = ocr_tool.extract_text_from_image(image)
            if text:
                ocr_tool.save_to_docx(text, output_path)
                return jsonify({"message": "Text extracted from image and saved successfully!", "text": text}), 200
            else:
                return jsonify({"error": "Failed to extract text from image."}), 500
        elif 'pdf' in request.files:
            pdf = request.files['pdf']
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_pdf:
                pdf.save(tmp_pdf)
                text = ocr_tool.extract_text_from_pdf(tmp_pdf.name)
            if text:
                os.unlink(tmp_pdf.name)  # Delete the temporary file
                return jsonify({"message": "Text extracted from PDF successfully!", "text": text}), 200
            else:
                os.unlink(tmp_pdf.name)  # Delete the temporary file
                return jsonify({"error": "Failed to extract text from PDF."}), 500
        else:
            return jsonify({"error": "No image or PDF file provided."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

