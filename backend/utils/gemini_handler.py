from services.gemini_client import calificar_similitud_llm

def coordinar_peticion(aplicante: str, vacante: str):

    score = calificar_similitud_llm(aplicante, vacante)
    # Asignar estado en función del score
    if score <= 0.55:
        estado_id = 2  # Rechazado
    elif score >= 0.65:
        estado_id = 1  # Aceptado
    else:
        estado_id = 3  # Por revisar
    
    return estado_id