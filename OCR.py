import pytesseract
from PIL import Image
import fitz  # PyMuPDF
from docx import Document
from textblob import TextBlob
import config 

pytesseract.pytesseract.tesseract_cmd = config.TESSERACT_PATH
class ocr:
        
    def pdf_to_images(self, pdf_path):
        pdf_document = fitz.open(pdf_path)
        images = []
        for page_number in range(len(pdf_document)):
            page = pdf_document.load_page(page_number)
            pixmap = page.get_pixmap()
            
            # Convert the pixmap to a PIL image
            pil_image = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)
            images.append(pil_image)
        return images
    
    # OCR Development img to txt
    def extract_text_from_image(self,image_path):
        try:
            text = pytesseract.image_to_string(image_path)
            return self.preprocess_text(text)
        except Exception as e:
            print(f"Error in OCR: {e}")
            return None
        
    def extract_text_from_pdf(self,pdf_path):
        pil_images = self.pdf_to_images(pdf_path)
        text = ' '
        try:
            for pil_image in pil_images:
                text += '\n'*3 + pytesseract.image_to_string(pil_image)
            # return self.preprocess_text(text)
            return text
        except Exception as e:
            print(f"Error in OCR: {e}")
            return None
    # 
    def preprocess_text(self, text):
        return str(TextBlob(text).correct())
    # saving two documents Extracted_Text
    def save_to_docx(self, text, output_path):
        doc1 = Document()
        doc1.add_paragraph(text)
        doc1.save(output_path + 'Extracted_Text.docx')