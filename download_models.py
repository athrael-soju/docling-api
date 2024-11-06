import tempfile
from docling.document_converter import DocumentConverter

converter = DocumentConverter()
try:
    with tempfile.NamedTemporaryFile(delete=True) as temp_file:
        temp_file.write(b"Hello, World!")
        temp_file_path = temp_file.name
        converter.convert(temp_file_path)
except Exception as e:
    print(e)
