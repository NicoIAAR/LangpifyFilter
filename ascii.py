import re
import string

def limpiar_ascii(texto):
    # Elimina caracteres de control ASCII (0-31 y 127)
    texto_limpio = re.sub(r'[\x00-\x1F\x7F]', '', texto)
    # Opcional: elimina caracteres no imprimibles extendidos
    texto_limpio = ''.join(c for c in texto_limpio if c in string.printable)
    return texto_limpio

def contiene_ascii_sospechoso(texto):
    # Busca caracteres de control o no imprimibles
    return bool(re.search(r'[\x00-\x1F\x7F]', texto))

if __name__ == "__main__":
    prompt = input("Introduce el prompt para el LLM: ")
    if contiene_ascii_sospechoso(prompt):
        print("¡Advertencia! El prompt contiene caracteres ASCII sospechosos.")
        prompt = limpiar_ascii(prompt)
        print("Prompt limpio:", prompt)
    else:
        print("Prompt seguro:", prompt)