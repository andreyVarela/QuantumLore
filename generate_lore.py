from google import genai

#! API KEY (pasar a .env luego)
client = genai.Client(api_key="AIzaSyDYsZkqjhp96mAbRYTZYSJ1yJk_DF4ngvE")
model = "gemini-2.5-flash"

def generate_lore(universo):

    prompt = f"""
    Eres un generador experto de lore para juegos de fantasía y ciencia ficción.

    Por favor, crea un lore detallado y narrativo para un universo llamado "{nombre_universo}". La temática principal de este universo es: {tematica}.

    Cuenta una historia breve que explique el origen y el conflicto central de este mundo.

    Luego, genera los siguientes elementos:

    1. {num_personajes} personajes principales. Para cada personaje incluye:
    - Nombre
    - Rol o profesión
    - Descripción detallada de su personalidad y apariencia
    - Motivaciones y conflictos internos
    - Habilidades especiales o poderes

    2. {num_facciones} facciones relevantes. Para cada facción incluye:
    - Nombre
    - Ideales principales
    - Objetivos
    - Relación con otras facciones

    3. {num_misiones} misiones épicas. Para cada misión incluye:
    - Título
    - Descripción detallada
    - Objetivo principal
    - Recompensas o consecuencias al completarla

    4. {num_ubicaciones} ubicaciones importantes. Para cada ubicación incluye:
    - Nombre
    - Descripción vívida del entorno y la atmósfera
    - Relevancia dentro de la historia

    Presenta todo organizado en secciones con títulos claros. Usa un estilo inmersivo y evocador, como si fuera una enciclopedia de este mundo.
    """
    response = client.models.generate_content(
        model=model,
        contents=prompt
    )
    print(response)
    return response.text

print(generate_lore("2077 Planet city"))