import PyPDF2
from typing import BinaryIO, Union
import os

def extraer_texto_pdf(pdf_path: Union[str, BinaryIO]) -> str:
    """
    Extrae el texto de un archivo PDF.
    Args:
        pdf_path (Union[str, BinaryIO]): Ruta al archivo PDF o archivo abierto
    Returns:
        str: El texto extraído del PDF.
    """
    texto = ""
    
    # Si es una ruta de archivo (string)
    if isinstance(pdf_path, str):
        try:
            lector_pdf = PyPDF2.PdfReader(pdf_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"No se encontró el archivo en: {os.path.abspath(pdf_path)}")
    else:
        # Si es un archivo ya abierto
        lector_pdf = PyPDF2.PdfReader(pdf_path)
    
    # Procesar todas las páginas
    for pagina in lector_pdf.pages:
        texto += pagina.extract_text() or ""
    
    return texto.strip()