import PyPDF2

def extract_text(file):
    pdf = PyPDF2.PdfReader(file)
    text = ""
    
    for page in pdf.pages:
        text += page.extract_text()
    
    return text.lower()