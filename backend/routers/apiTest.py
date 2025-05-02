from fastapi import APIRouter, Depends, HTTPException
import os
from utils.pdf_utils import extraer_texto_pdf
from utils.gemini_handler import coordinar_peticion

router = APIRouter(
    prefix="/test",
    tags=["test"],
    responses={404: {"description": "Not found"}},
)

@router.get("/extraer-texto-prueba")
def extraer_texto_pdf_prueba():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pdf_path = os.path.join(base_dir, 'test_pdfs', 'entrega.pdf')
    try:
        texto = extraer_texto_pdf(pdf_path)
        return {"texto": texto}
    except Exception as e:
        print(f"Error al procesar el PDF: {e}")
        return {"error": str(e)}
    
@router.get("/evaluar/")
def evaluar():
    return coordinar_peticion()
