import os
from cloudflare import Cloudflare
import random
import generate_lore_prompt
#! API KEY (pasar a .env luego)


acount_id = "36a986f20bee29ef1a6c96b304a202c1"

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

def principal():
    nombre_universo=str(input("Introduce el nombre del universo: "))
    tematica = str(input("Introduce la temática del universo (fantasía, ciencia ficción, etc.): "))
    num_personajes = random.randint(5, 10)
    num_facciones = random.randint(3, 5)
    num_misiones = random.randint(2, 4)
    num_ubicaciones = random.randint(3, 6)
    #generate_lore_image(nombre_universo)
    #lore = ''#!temporal
    responseText = generate_lore_prompt.generate_lore(nombre_universo, tematica, num_personajes, num_facciones, num_misiones, num_ubicaciones)
    print(f"\n✅ response '{responseText}'...\n")
    lore = responseText[0]  # Lore text
    print(f"\n✅ Historia generada para '{lore}':\n")
    promptToImg = responseText[1]  # Prompt for image generation
        # Guardar en archivo de texto
    filename = f"{nombre_universo.replace(' ', '_').lower()}_lore.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(lore)
    
    print(f"\n✅ Historia guardada en '{filename}'")
    print(f"\n✅ prompt '{promptToImg}'")
if __name__ == "__main__":
    principal()