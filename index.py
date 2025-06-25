import re

def limpiar_input(user_input):
    # Solo permite letras, números y espacios
    texto_limpio = re.sub(r'[^a-zA-Z0-9 ]', '', user_input)
    # Elimina palabras peligrosas
    palabras_prohibidas = [r'DATABASE', r'base de datos', r'SQL', r'SELECT', r'UPDATE', r'GET', r'DELETE', r'POST', r'PUT', r'TABLE', r'GROUP BY', r'ORDER BY', r'INSERT', r'mysql',r'mongodb', r'password', r'username', r'user', r'pass', r'root', r'admin', r'contraseña']
    for palabra in palabras_prohibidas:
        # Elimina la palabra, sin importar mayúsculas/minúsculas
        texto_limpio = re.sub(palabra, '', texto_limpio, flags=re.IGNORECASE)
    return texto_limpio

if __name__ == "__main__":
    entrada = input("Introduce un texto: ")
    limpio = limpiar_input(entrada)
    print(f"Texto limpio: {limpio}")

