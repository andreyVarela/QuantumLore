from google import genai

#! API KEY (pasar a .env luego)
client = genai.Client(api_key="AIzaSyDYsZkqjhp96mAbRYTZYSJ1yJk_DF4ngvE")
model = "gemini-2.5-flash"

def generate_lore(universo):

    prompt = f"""
Eres un generador experto de lore para juegos de fantasía y ciencia ficción.

Por favor, crea un lore detallado para un universo llamado "{universo}". Incluye:

1. Cinco personajes principales, cada uno con:
    - Nombre
    - Rol
    - Descripción breve
    - Motivaciones
    - Habilidades especiales

2. Tres facciones importantes con:
    - Nombre
    - Ideales principales
    - Objetivos

3. Tres misiones épicas con:
    - Título
    - Descripción
    - Recompensas

4. Cuatro ubicaciones relevantes con:
    - Nombre
    - Descripción detallada
    - Relevancia en la historia

Presenta todo bien organizado en secciones con títulos claros.
"""
    response = client.models.generate_content(
        model=model,
        contents=prompt
    )
    print(response)
    return response.text

print(generate_lore("2077 Planet city"))