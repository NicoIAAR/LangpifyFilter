#Langpify Filter
import re

def limpiar_entrada(entrada_usuario):
    """
    Limpia el texto de entrada eliminando palabras peligrosas,
    permitiendo solo caracteres seguros (incluyendo español, francés, portugués, chino y japonés).
    """
    # Lista de strings que deben eliminarse completamente
    strings_vacios = ['1=1', '2=2', '3=3', '4=4', '5=5', '6=6', '7=7', '8=8', '9=9''@@version', '@@hostname', '@@datadir', '@@tmpdir', '@@basedir', '@@innodb_version', '@@version_compile_os', 'root@', 'xp_', '.dmg', '.exe']
    texto_limpio = entrada_usuario
    for cadena in strings_vacios:
        texto_limpio = texto_limpio.replace(cadena, '')
    
    # Permitir solo letras (con acentos, diéresis, ñ, ç, ã, õ, ê, â, ô, î, û, à, è, ù, ë, ï, ö, ü, œ, æ, ÿ, ç, Ç), números, espacios, comas, puntos y caracteres Chinos y Japoneses
    texto_limpio = re.sub(r'[^a-zA-Z0-9 áéíóúÁÉÍÓÚüÜñÑãõÃÕâêîôûÂÊÎÔÛàèùÀÈÙëïöüËÏÖÜœŒæÆÿŸçÇ\u4e00-\u9fff\u3040-\u30ff\u3400-\u4dbf,.]', '', texto_limpio)
    # Remove dangerous words
    palabras_prohibidas = [
        'DATABASE', 'base de datos','mysql', 'SQL', 'SELECT', 'UPDATE', 'GET', 'DELETE', 'POST', 'PUT', 'TABLE', 'GROUP BY', 'ORDER BY', 'INSERT',
        'INNER JOIN', 'mongodb', 'mongo', 'mongod', 'mongoose', 'password', 'username', 'user', 'pass', 'root', 'admin', 'contraseña', 'ignore',
        'Ignore previous instructions', 'ignorar instrucciones previas', 'inspect', 'html', 'xss', 'iframe', 'script', 'ssh', 'http', 'https', 'localhost', 'hostname',
        'cookie', 'cookies', 'function', 'void', 'xhr', 'php', 'htmlentities', 'alert', 'xml',
        'drop', 'truncate', 'alter', 'create', 'grant', 'revoke', 'union', 'cast', 'char', 'varchar', 'where', 'from', 'into', 'values',
        '--', '#', ';', ' between ', 'count', 'benchmark', 'sleep', 'waitfor', 'xp_', '0x',
        'load_file', 'outfile', 'dumpfile', 'shutdown', 'exec', 'execute', 'xp_cmdshell', 'openrowset', 'openquery', 'sysobjects', 'syscolumns',
        'information_schema', 'pg_', 'pg_catalog', 'current_user', 'session_user', 'system_user', 'pg_sleep', 'pg_terminate_backend',
        'file_priv', 'exploit', 'wget', 'hydra', 'nmap', '0x', 'benchmark',  'bash'
    ]
    # Agrega el prefijo r'' por cada palabra
    palabras_prohibidas = [r'' + palabra for palabra in palabras_prohibidas]
    for palabra in palabras_prohibidas:
        # Eliminar la palabra, sin importar mayúsculas/minúsculas
        texto_limpio = re.sub(palabra, '', texto_limpio, flags=re.IGNORECASE)
    
    # Eliminar espacios redundantes
    texto_limpio = re.sub(r'\s+', ' ', texto_limpio).strip()
    return texto_limpio

if __name__ == "__main__":
    entrada = input("Ingrese un texto: ")
    texto_limpio = limpiar_entrada(entrada)
    print(f"Texto limpio: {texto_limpio}")


