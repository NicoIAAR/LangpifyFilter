import re

def limpiar_input(user_input):
    # Solo permite letras (incluyendo acentos, diéresis y ñ), números y espacios
    texto_limpio = re.sub(r'[^a-zA-Z0-9 áéíóúÁÉÍÓÚüÜñÑ]', '', user_input)
    # Elimina palabras peligrosas
    palabras_prohibidas = [
        r'DATABASE', r'base de datos', r'SQL', r'SELECT', r'UPDATE', r'GET', r'DELETE', r'POST', r'PUT', r'TABLE', r'GROUP BY', r'ORDER BY', r'INSERT',
        r'INNER JOIN', r'mysql', r'mongodb', r'mongo', r'mongod', r'mongoose', r'password', r'username', r'user', r'pass', r'root', r'admin', r'contraseña',
        r'Ignore previous instructions', r'ignorar instrucciones previas', r'inspect', r'html', r'xss', r'iframe', r'script', r'http', r'https', r'localhost',
        r'cookie', r'cookies', r'function', r'void', r'xhr', r'php', r'htmlentities', r'alert', r'xml',
        r'drop', r'truncate', r'alter', r'create', r'grant', r'revoke', r'union', r'cast', r'char', r'varchar', r'where', r'from', r'into', r'values',
        r'--', r'#', r';', r' or ', r' and ', r' not ', r' like ', r' between ', r'count', r'benchmark', r'sleep', r'waitfor', r'xp_', r'0x',
        r'load_file', r'outfile', r'dumpfile', r'shutdown', r'exec', r'execute', r'xp_cmdshell', r'openrowset', r'openquery', r'sysobjects', r'syscolumns',
        r'information_schema', r'pg_', r'pg_catalog', r'current_user', r'session_user', r'system_user', r'pg_sleep', r'pg_terminate_backend',
        r'@@version', r'@@hostname', r'@@datadir', r'@@tmpdir', r'@@basedir', r'@@innodb_version', r'@@version_compile_os',
        r'file_priv', r'root@', r'0=0', r'1=1', r'2=2', r'3=3', r'4=4', r'5=5', r'6=6', r'7=7', r'8=8', r'9=9'
    ]
    for palabra in palabras_prohibidas:
        # Elimina la palabra, sin importar mayúsculas/minúsculas
        texto_limpio = re.sub(palabra, '', texto_limpio, flags=re.IGNORECASE)
    return texto_limpio

if __name__ == "__main__":
    entrada = input("Introduce un texto: ")
    limpio = limpiar_input(entrada)
    print(f"Texto limpio: {limpio}")

