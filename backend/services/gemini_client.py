import google.generativeai as genai
from google.generativeai import list_models

def calificar_similitud_llm(cv_texto: str, vacante_texto: str) -> float:
    """
    Evalúa la similitud entre un CV y una vacante utilizando el modelo Gemini 2.0 Flash.
    Devuelve un valor decimal entre 0 y 1 representando el grado de ajuste.
    """
    model = genai.GenerativeModel('gemini-2.0-flash')
    genai.configure(api_key='')

    prompt = f"""
Eres un experto seleccionador de personal. Tu tarea es analizar cuidadosamente si una hoja de vida se ajusta al perfil de una vacante.

Instrucciones:
1. Analiza la información que se te entrega de ambos textos.
2. Evalúa qué tan bien se ajusta el perfil de la hoja de vida a los requisitos de la vacante.
3. Devuelve **solo** un número decimal entre 0 y 1, donde 1 significa que es un encaje perfecto y 0 que no tiene ninguna relación.

Ejemplo de formato esperado: 0.74 (nada más, sin comentarios ni explicaciones).

Texto de la vacante:
\"\"\"
{vacante_texto}
\"\"\"

Texto del candidato:
\"\"\"
{cv_texto}
\"\"\"

Recuerda: devuelve solo un número decimal entre 0 y 1.
"""

    try:
        response = model.generate_content(prompt)
        # Intenta convertir la respuesta directamente a float
        try:
            return float(response.text)
        except ValueError:
            raise ValueError(f"La respuesta del modelo no es un número válido: '{response.text}'")
    except Exception as e:
        raise ValueError(f"Error al generar la respuesta del modelo: {e}")