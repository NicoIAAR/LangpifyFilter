#Langpify Filter
import re

class LangpifyFilter:
    """
    Una clase para limpiar y sanear entradas de texto, eliminando patrones
    y palabras potencialmente peligrosas para sistemas como LLMs.
    """
    # Tuplas de configuración inmutables
    STRINGS_A_ELIMINAR = (
        '1=1', '2=2', '3=3', '4=4', '5=5', '6=6', '7=7', '8=8', '9=9', '@@version', 
        '@@hostname', '@@datadir', '@@tmpdir', '@@basedir', '@@innodb_version', 
        '@@version_compile_os', 'root@', 'xp_', '.dmg', '.exe', '*'
    )
    
    PALABRAS_PROHIBIDAS = (
        'DATABASE', 'base de datos', 'mysql', 'SQL', 'SELECT', 'UPDATE', 'GET', 'DELETE', 'POST', 'PUT', 
        'TABLE', 'GROUP BY', 'ORDER BY', 'INSERT', 'INNER JOIN', 'mongodb', 'mongo', 'mongod', 'mongoose', 
        'password', 'username', 'user', 'pass', 'root', 'admin', 'contraseña', 'ignore', 
        'Ignore previous instructions', 'ignorar instrucciones previas', 'inspect', 'html', 'xss', 'iframe', 
        'script', 'ssh', 'http', 'https', 'localhost', 'hostname', 'cookie', 'cookies', 'function', 'void', 
        'xhr', 'php', 'htmlentities', 'alert', 'xml', 'drop', 'truncate', 'alter', 'create', 'grant', 
        'revoke', 'union', 'cast', 'char', 'varchar', 'where', 'from', 'into', 'values', '--', '#', ';', 
        ' between ', 'count', 'benchmark', 'sleep', 'waitfor', 'xp_', '0x', 'load_file', 'outfile', 'dumpfile', 
        'shutdown', 'exec', 'execute', 'xp_cmdshell', 'openrowset', 'openquery', 'sysobjects', 'syscolumns', 
        'information_schema', 'pg_', 'pg_catalog', 'current_user', 'session_user', 'system_user', 
        'pg_sleep', 'pg_terminate_backend', 'file_priv', 'exploit', 'wget', 'hydra', 'nmap', 'bash', 'curl'
    )

    # Regex pre-compilado para caracteres permitidos
    REGEX_CARACTERES_SEGUROS = re.compile(
        r'[^a-zA-Z0-9 áéíóúÁÉÍÓÚüÜñÑãõÃÕâêîôûÂÊÎÔÛàèùÀÈÙëïöüËÏÖÜœŒæÆÿŸçÇ'
        r'\u4e00-\u9fff\u3040-\u30ff\u3400-\u4dbf,.]'
    )

    def __init__(self):
        """
        Inicializa el filtro compilando un único patrón de regex para todas
        las palabras prohibidas, mejorando el rendimiento.
        """
        # Escapamos cada palabra para que se trate como un literal en el regex
        patron_prohibido = '|'.join(re.escape(palabra) for palabra in self.PALABRAS_PROHIBIDAS)
        self.regex_prohibido = re.compile(patron_prohibido, re.IGNORECASE)

    def limpiar(self, entrada_usuario):
        """
        Limpia el texto de entrada aplicando todas las reglas de filtrado.
        """
        texto_limpio = entrada_usuario

        # 1. Eliminar strings específicos usando reemplazo simple
        for cadena in self.STRINGS_A_ELIMINAR:
            texto_limpio = texto_limpio.replace(cadena, '')
        
        # 2. Permitir solo caracteres seguros de la whitelist
        texto_limpio = self.REGEX_CARACTERES_SEGUROS.sub('', texto_limpio)
        
        # 3. Eliminar todas las palabras prohibidas de una sola vez
        texto_limpio = self.regex_prohibido.sub('', texto_limpio)
        
        # 4. Normalizar espacios en blanco
        texto_limpio = re.sub(r'\s+', ' ', texto_limpio).strip()
        
        return texto_limpio

if __name__ == "__main__":
    filtro = LangpifyFilter()
    entrada = input("Ingrese un texto: ")
    texto_limpio = filtro.limpiar(entrada)
    print(f"Texto limpio: {texto_limpio}")


