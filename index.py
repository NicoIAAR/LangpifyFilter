#Langpify Filter
import re

def clean_input(user_input):
    # Replace specific strings with empty string first
    empty_strings = ['1=1', '2=2', '3=3', '4=4', '5=5', '6=6', '7=7', '8=8', '9=9']
    clean_text = user_input
    for empty_str in empty_strings:
        clean_text = clean_text.replace(empty_str, '')
    
    # Allow only letters (including accents, dieresis, ñ, ç, ã, õ, ê, â, ô, î, û, à, è, ù, ë, ï, ö, ü, œ, æ, ÿ, ç, Ç), numbers, spaces, commas, periods, and CJK (Chinese, Japanese, Korean) characters
    clean_text = re.sub(r'[^a-zA-Z0-9 áéíóúÁÉÍÓÚüÜñÑãõÃÕâêîôûÂÊÎÔÛàèùÀÈÙëïöüËÏÖÜœŒæÆÿŸçÇ\u4e00-\u9fff\u3040-\u30ff\u3400-\u4dbf,.]', '', clean_text)
    # Remove dangerous words
    forbidden_words = [
        'DATABASE', 'base de datos','mysql', 'SQL', 'SELECT', 'UPDATE', 'GET', 'DELETE', 'POST', 'PUT', 'TABLE', 'GROUP BY', 'ORDER BY', 'INSERT',
        'INNER JOIN', 'mongodb', 'mongo', 'mongod', 'mongoose', 'password', 'username', 'user', 'pass', 'root', 'admin', 'contraseña', 'ignore',
        'Ignore previous instructions', 'ignorar instrucciones previas', 'inspect', 'html', 'xss', 'iframe', 'script', 'ssh', 'http', 'https', 'localhost', 'hostname',
        'cookie', 'cookies', 'function', 'void', 'xhr', 'php', 'htmlentities', 'alert', 'xml',
        'drop', 'truncate', 'alter', 'create', 'grant', 'revoke', 'union', 'cast', 'char', 'varchar', 'where', 'from', 'into', 'values',
        '--', '#', ';', ' like ', ' between ', 'count', 'benchmark', 'sleep', 'waitfor', 'xp_', '0x',
        'load_file', 'outfile', 'dumpfile', 'shutdown', 'exec', 'execute', 'xp_cmdshell', 'openrowset', 'openquery', 'sysobjects', 'syscolumns',
        'information_schema', 'pg_', 'pg_catalog', 'current_user', 'session_user', 'system_user', 'pg_sleep', 'pg_terminate_backend',
        '@@version', '@@hostname', '@@datadir', '@@tmpdir', '@@basedir', '@@innodb_version', '@@version_compile_os',
        'file_priv', 'root@', 'exploit', 'wget', 'hydra', 'nmap', '.exe', 'xp_', '0x', 'benchmark'
    ]
    # Add r'' prefix to each word (for regex)
    forbidden_words = [r'' + word for word in forbidden_words]
    for word in forbidden_words:
        # Remove the word, case insensitive
        clean_text = re.sub(word, '', clean_text, flags=re.IGNORECASE)
    
    return clean_text

if __name__ == "__main__":
    entry = input("Enter a text: ")
    cleaned = clean_input(entry)
    print(f"Cleaned text: {cleaned}")


