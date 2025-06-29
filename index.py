#Langpify Filter
import re

def limpiar_input(user_input):
    # Reemplazar strings específicos con '' primero
    strings_vacios = ['1=1', '2=2', '3=3', '4=4', '5=5', '6=6', '7=7', '8=8', '9=9']
    texto_limpio = user_input
    for string_vacio in strings_vacios:
        texto_limpio = texto_limpio.replace(string_vacio, '')
    
    # Solo permite letras (incluyendo acentos, diéresis y ñ), números y espacios
    texto_limpio = re.sub(r'[^a-zA-Z0-9 áéíóúÁÉÍÓÚüÜñÑ]', '', texto_limpio)
    # Elimina palabras peligrosas
    palabras_prohibidas = [
        'DATABASE', 'base de datos','mysql', 'SQL', 'SELECT', 'UPDATE', 'GET', 'DELETE', 'POST', 'PUT', 'TABLE', 'GROUP BY', 'ORDER BY', 'INSERT',
        'INNER JOIN', 'mongodb', 'mongo', 'mongod', 'mongoose', 'password', 'username', 'user', 'pass', 'root', 'admin', 'contraseña', 'ignore',
        'Ignore previous instructions', 'ignorar instrucciones previas', 'inspect', 'html', 'xss', 'iframe', 'script', 'http', 'https', 'localhost', 'hostname',
        'cookie', 'cookies', 'function', 'void', 'xhr', 'php', 'htmlentities', 'alert', 'xml',
        'drop', 'truncate', 'alter', 'create', 'grant', 'revoke', 'union', 'cast', 'char', 'varchar', 'where', 'from', 'into', 'values',
        '--', '#', ';', ' or ', ' and ', ' not ', ' like ', ' between ', 'count', 'benchmark', 'sleep', 'waitfor', 'xp_', '0x',
        'load_file', 'outfile', 'dumpfile', 'shutdown', 'exec', 'execute', 'xp_cmdshell', 'openrowset', 'openquery', 'sysobjects', 'syscolumns',
        'information_schema', 'pg_', 'pg_catalog', 'current_user', 'session_user', 'system_user', 'pg_sleep', 'pg_terminate_backend',
        '@@version', '@@hostname', '@@datadir', '@@tmpdir', '@@basedir', '@@innodb_version', '@@version_compile_os',
        'file_priv', 'root@'
    ]
    # Agregar el prefijo r'' a cada palabra
    palabras_prohibidas_o = [f"r'{palabra}'" for palabra in palabras_prohibidas]
    for palabra in palabras_prohibidas:
        # Elimina la palabra, sin importar mayúsculas/minúsculas
        texto_limpio = re.sub(palabra, '', texto_limpio, flags=re.IGNORECASE)
    
    return texto_limpio

if __name__ == "__main__":
    entrada = input("Introduce un texto: ")
    limpio = limpiar_input(entrada)
    print(f"Texto limpio: {limpio}")


