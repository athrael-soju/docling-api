import io

from fastapi import FastAPI, File, UploadFile
from docling.document_converter import DocumentConverter
from docling.datamodel.base_models import DocumentStream
from pydantic import BaseModel
from pypdf import PdfReader, PdfWriter


class ConvertResponse(BaseModel):
    text: str | None = None


class ConvertPagesResponse(BaseModel):
    texts: list[str] = []


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/convert")
async def convert(file: UploadFile = File(...)) -> ConvertResponse:
    converter = DocumentConverter()
    md_result = None
    with io.BytesIO() as stream:
        stream.write(await file.read())
        stream.seek(0)
        res = converter.convert(DocumentStream(name=file.filename, stream=stream))
        md_result = res.document.export_to_markdown()
    return ConvertResponse(text=md_result)


@app.post("/convert_pages")
async def convert_pages(file: UploadFile = File(...)) -> ConvertPagesResponse:
    """
    Convert each page of the PDF file to markdown.
    """
    converter = DocumentConverter()
    sources: list[DocumentStream] = []
    reader = PdfReader(io.BytesIO(await file.read()))
    for i, page in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(page)
        stream = io.BytesIO()
        writer.write(stream)
        stream.seek(0)
        sources.append(DocumentStream(name=f"page-{i}.pdf", stream=stream))
    results = converter.convert_all(sources, raises_on_error=False)
    md_result = ConvertPagesResponse()
    for result in results:
        md_result.texts.append(result.document.export_to_markdown())
    return md_result
