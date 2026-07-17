import fitz
from docx import Document


def extract_text_from_pdf(uploaded_file):
    document = fitz.open(
        stream=uploaded_file.getvalue(),
        filetype="pdf"
    )

    text = ""

    for page in document:
        text += page.get_text()

    return text


def extract_text_from_docx(uploaded_file):
    document = Document(uploaded_file)
    paragraphs = []

    for paragraph in document.paragraphs:
        paragraphs.append(paragraph.text)

    return "\n".join(paragraphs)