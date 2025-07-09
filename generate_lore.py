from google import genai
import os
from cloudflare import Cloudflare
import random

#! API KEY (pasar a .env luego)
client = genai.Client(api_key="AIzaSyDYsZkqjhp96mAbRYTZYSJ1yJk_DF4ngvE")
model = "gemini-2.5-flash"
acount_id = "36a986f20bee29ef1a6c96b304a202c1"
def generate_lore(nombre_universo, tematica, num_personajes, num_facciones, num_misiones, num_ubicaciones):

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
    #image = generate_lore_image(response.text)

    return response.text#, image

def generate_lore_image(prompt):
    prompt = f"""
    Crea una imagen que represente esta historia: {prompt}
    """

    client = Cloudflare(
    api_token=os.environ.get("g1u0rdzN4oisEmlYuJZ6kUt0xgZdAw9JaapYbFLw"),  # This is the default and can be omitted
)
    response = client.ai.run(
        model_name="model_name",
        account_id=acount_id,
        text=prompt,
    )
    return response.image_url

def main():
    nombre_universo=str(input("Introduce el nombre del universo: "))
    tematica = str(input("Introduce la temática del universo (fantasía, ciencia ficción, etc.): "))
    num_personajes = random.randint(5, 10)
    num_facciones = random.randint(3, 5)
    num_misiones = random.randint(2, 4)
    num_ubicaciones = random.randint(3, 6)

    lore = generate_lore(nombre_universo, tematica, num_personajes, num_facciones, num_misiones, num_ubicaciones)
        # Guardar en archivo de texto
    filename = f"{nombre_universo.replace(' ', '_').lower()}_lore.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(lore)
    
    print(f"\n✅ Historia guardada en '{filename}'")

if __name__ == "__main__":
    main()