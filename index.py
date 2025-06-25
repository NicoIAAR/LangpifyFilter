import re

def limpiar_input(user_input):
    # Solo permite letras, números y espacios
    texto_limpio = re.sub(r'[^a-zA-Z0-9 ]', '', user_input)
    # Elimina palabras peligrosas
    palabras_prohibidas = [r'database', r'base de datos', r'sql']
    for palabra in palabras_prohibidas:
        # Elimina la palabra, sin importar mayúsculas/minúsculas
        texto_limpio = re.sub(palabra, '', texto_limpio, flags=re.IGNORECASE)
    return texto_limpio

if __name__ == "__main__":
    entrada = input("Introduce un texto: ")
    limpio = limpiar_input(entrada)
    print(f"Texto limpio: {limpio}")

