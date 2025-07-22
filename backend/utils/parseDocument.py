from fastapi import FastAPI, UploadFile, File, HTTPException
from pathlib import Path
from io import BytesIO

from docx import Document
import fitz  # PyMuPDF

app = FastAPI()

def parse_txt(file_obj: BytesIO):
    return file_obj.read().decode('utf-8')

def parse_docx(file_obj: BytesIO):
    doc = Document(file_obj)
    return "\n".join(p.text for p in doc.paragraphs)

def parse_pdf(file_obj: BytesIO):
    pdf_data = fitz.open(stream=file_obj.read(), filetype="pdf")
    return "\n".join(page.get_text() for page in pdf_data)

def parse_uploaded_file(file_obj: BytesIO, filename: str) -> str:
    ext = Path(filename).suffix.lower()
    file_obj.seek(0)

    if ext == '.txt':
        return parse_txt(file_obj)
    elif ext == '.docx':
        return parse_docx(file_obj)
    elif ext == '.pdf':
        return parse_pdf(file_obj)
    else:
        raise ValueError(f"Unsupported file type: {ext}")

async def parse_file(file: UploadFile = File(None)):
    ext = Path(file.filename).suffix.lower()
    if ext not in [".txt", ".docx", ".pdf"]:
        raise HTTPException(status_code=400, detail="Only .txt, .docx, and .pdf files are supported.")

    try:
        file_bytes = BytesIO( await file.read())
        parsed_text = parse_uploaded_file(file_bytes, file.filename)
        print(parsed_text)
        return parsed_text
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
