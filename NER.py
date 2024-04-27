from docx import Document
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline


class ner_tagger:
    def __init__(self) -> None:

        self.tokenizer = AutoTokenizer.from_pretrained("xlm-roberta-large-finetuned-conll03-english")
        self.model = AutoModelForTokenClassification.from_pretrained("xlm-roberta-large-finetuned-conll03-english")
        self.ner = pipeline("ner", model=self.model, tokenizer=self.tokenizer)

    def ner_extraction(self, text):
        # print(text)
        try:
            entities = self.ner(text)
            return entities
        except Exception as e:
            print(f"Error in NER: {e}")
            return None
        
    def decode_ner(self,tuples):
        entityes = {}
        # print(tuples)
        for tag, chunk in tuples:
            if chunk[0] == '▁':
                if tag in entityes:
                    entityes[tag].append(chunk[1:])
                else:
                    entityes[tag] = [chunk[1:]]
            elif tag in entityes:
                entityes[tag][-1] += chunk
        return entityes
    
    # saving documents Named Entities as list
    def save_to_docx(self, entities, output_path):       
        doc2 = Document()
        ent = [(e['entity'],e['word']) for e in entities if e['score'] > 0.5]
        # print(ent)
        doc2.add_paragraph(str(ent))
        doc2.save(output_path + 'Named Entities.docx')