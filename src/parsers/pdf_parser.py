import PyPDF2

class PDFParser:
    def extract_text(self, pdf_file):
        # pdf_file is a file-like object (Streamlit UploadedFile)
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text