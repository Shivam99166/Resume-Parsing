import io
from typing import Union
import pdfplumber
async def extract_text_from_pdf(file_bytes: Union[bytes, bytearray]) -> str:
    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        text = ""
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text