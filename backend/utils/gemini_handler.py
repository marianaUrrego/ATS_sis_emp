from services.gemini_client import calificar_similitud_llm

def coordinar_peticion(list_aplicantes: list[str], vacante: str):
        return [(aplicante, calificar_similitud_llm(aplicante, vacante)) for aplicante in list_aplicantes]
    
    

    
    
    
    
    
    
    
