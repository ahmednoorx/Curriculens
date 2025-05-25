from fpdf import FPDF

class PDFExporter:
    def export(self, content, filename):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        for line in content.splitlines():
            pdf.cell(200, 10, txt=line, ln=True)
        
        pdf.output(filename)