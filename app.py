import tempfile

from fastapi import FastAPI, File, UploadFile
from docling.document_converter import DocumentConverter
from pydantic import BaseModel


class ConvertResponse(BaseModel):
    text: str | None = None


app = FastAPI()

@app.post("/convert")
async def convert(file: UploadFile = File(...)) -> ConvertResponse:
    converter = DocumentConverter()
    md_result = None
    with tempfile.NamedTemporaryFile(delete=True) as temp_file:
        temp_file.write(await file.read())
        temp_file_path = temp_file.name
        res = converter.convert(temp_file_path)
        md_result = res.document.export_to_markdown()
    return ConvertResponse(text=md_result)
