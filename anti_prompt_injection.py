import re

# Lista de patrones comunes de prompt injection (puedes ampliarla)
PATRONES_SOSPECHOSOS = [
    r"(?i)ignore previous instructions",  # Ignorar instrucciones previas
    r"(?i)forget all previous",           # Olvidar todo lo anterior
    r"(?i)you are now",                  # Cambiar de rol
    r"(?i)act as",                       # Actuar como
    r"(?i)system:.*",                    # Instrucciones de sistema
    r"(?i)assistant:.*",                 # Instrucciones al asistente
    r"(?i)user:.*",                      # Instrucciones al usuario
    r"(?i)\[.*?\]",                    # Uso de corchetes para instrucciones
    r"(?i)```.*?```",                    # Bloques de código sospechosos
]

def detectar_prompt_injection(texto):
    """Devuelve True si detecta patrones sospechosos de prompt injection."""
    for patron in PATRONES_SOSPECHOSOS:
        if re.search(patron, texto):
            return True
    return False

def limpiar_prompt(texto):
    """Elimina patrones sospechosos del texto."""
    texto_limpio = texto
    for patron in PATRONES_SOSPECHOSOS:
        texto_limpio = re.sub(patron, "[REMOVIDO]", texto_limpio, flags=re.DOTALL)
    return texto_limpio

if __name__ == "__main__":
    prompt = input("Introduce el prompt para el LLM: ")
    if detectar_prompt_injection(prompt):
        print("¡Advertencia! Se detectó posible prompt injection.")
        prompt_limpio = limpiar_prompt(prompt)
        print("Prompt limpio:", prompt_limpio)
    else:
        print("Prompt seguro:", prompt)
