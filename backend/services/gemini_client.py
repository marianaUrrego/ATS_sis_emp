import google.generativeai as genai
from google.generativeai import list_models

def calificar_similitud_llm(cv_texto: str, vacante_texto: str) -> float:
    """
    Evalúa la similitud entre un CV y una vacante utilizando el modelo Gemini 2.0 Flash.
    Devuelve un valor decimal entre 0 y 1 representando el grado de ajuste.
    """
    model = genai.GenerativeModel('gemini-2.0-flash')
    genai.configure(api_key='AIzaSyAeCoRh8rZDDRIvL93dDG_8mzXOPFZKd8k')

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
    
def obtener_nombre_correo_llm(cv_texto: str) -> dict:
    """
    Extrae el nombre y correo electrónico de un CV utilizando el modelo Gemini 2.0 Flash.
    
    Args:
        cv_texto (str): Texto del CV del que se extraerá la información.
        
    Returns:
        dict: Diccionario con las claves 'nombre' y 'correo' conteniendo la información extraída.
    """
    import google.generativeai as genai
    
    # Configurar el modelo
    model = genai.GenerativeModel('gemini-2.0-flash')
    genai.configure(api_key='AIzaSyAeCoRh8rZDDRIvL93dDG_8mzXOPFZKd8k')  # Asegúrate de configurar tu API key
    
    prompt = f"""
Eres un asistente especializado en extracción de información. Tu tarea es extraer el nombre completo y el correo electrónico de una hoja de vida.

Instrucciones:
1. Analiza cuidadosamente el texto de la hoja de vida proporcionado.
2. Identifica el nombre completo del candidato y su correo electrónico.
3. Devuelve ÚNICAMENTE un objeto JSON con la siguiente estructura:
   {{"nombre": "Nombre Completo", "correo": "correo@ejemplo.com"}}

Si no puedes identificar alguno de los campos, coloca una cadena vacía ("") en ese campo.

Texto de la hoja de vida:
\"\"\"
{cv_texto}
\"\"\"

Recuerda: Devuelve solo un objeto JSON con la estructura especificada, sin comentarios adicionales.
"""

    try:
        response = model.generate_content(prompt)
        response_text = response.text.strip()
        
        # Intentar extraer el JSON de la respuesta
        import json
        import re
        
        # Buscar un patrón JSON en la respuesta
        json_pattern = r'({.*})'
        match = re.search(json_pattern, response_text)
        
        if match:
            json_str = match.group(1)
            datos = json.loads(json_str)
            
            # Verificar que el diccionario tenga las claves requeridas
            if 'nombre' in datos and 'correo' in datos:
                return {
                    'nombre': datos['nombre'],
                    'correo': datos['correo']
                }
        
        # Si no se pudo extraer correctamente, intentar un parsing más manual
        nombre = ""
        correo = ""
        
        # Buscar un patrón de correo electrónico
        email_pattern = r'[\w.+-]+@[\w-]+\.[\w.-]+'
        email_match = re.search(email_pattern, response_text)
        if email_match:
            correo = email_match.group(0)
        
        # Si llegamos aquí, devolver lo que se pudo extraer
        return {
            'nombre': nombre,
            'correo': correo
        }
        
    except Exception as e:
        # En caso de error, devolver un diccionario vacío
        print(f"Error al extraer nombre y correo: {e}")
        return {
            'nombre': "",
            'correo': ""
        }