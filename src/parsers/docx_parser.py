class DOCXParser:
    def extract_text(self, docx_file):
        from docx import Document
        
        doc = Document(docx_file)
        text = []
        
        for paragraph in doc.paragraphs:
            text.append(paragraph.text)
        
        return '\n'.join(text)