import tempfile

from fastapi import FastAPI, File, UploadFile
from docling.document_converter import DocumentConverter


app = FastAPI()

@app.post("/convert")
async def convert(file: UploadFile = File(...)) -> str:
    converter = DocumentConverter()
    result = None
    with tempfile.NamedTemporaryFile(delete=True) as temp_file:
        temp_file.write(await file.read())
        temp_file_path = temp_file.name
        result = converter.convert(temp_file_path)
    return result
