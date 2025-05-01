import PyPDF2
from typing import BinaryIO

def extraer_texto_pdf(pdf_file: BinaryIO) -> str:
    """
    Extrae el texto de un archivo PDF.

    Args:
        pdf_file (BinaryIO): El archivo PDF del cual se extraerá el texto.

    Returns:
        str: El texto extraído del PDF.
    """
    texto = ""
    with PyPDF2.PdfReader(pdf_file) as lector_pdf:
        for pagina in lector_pdf.pages:
            texto += pagina.extract_text() or ""
    return texto.strip()