import PyPDF2

def extract_text(file):
    """
    Extract text from a PDF file uploaded via FastAPI.
    
    Args:
        file: UploadFile.file object
    
    Returns:
        str: Extracted text from the PDF
    """

    try:
        reader = PyPDF2.PdfReader(file)
        text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + " "

        # Clean up text
        text = text.lower().strip()

        return text

    except Exception as e:
        return f"Error reading PDF: {str(e)}"