import paramiko
import os
import logging
from logging.handlers import RotatingFileHandler



#----------------CONFIGURANDO MEU LOGGING ----------------------------------------

# Criação de um logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Caminho para salvar o arquivo de log
log_dir = os.path.join(os.getcwd(), 'Log')
log_file_path = os.path.join(log_dir, 'CargaSFTP.log')

# Verifica se a pasta Log existe, se não, cria
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Configuração do handler de log com rotação
handler = RotatingFileHandler(
    log_file_path, 
    maxBytes=2 * 1024 * 1024,  # 2 MB
    backupCount=4,  # Mantém até 5 arquivos de log (original + 4 backups)
    encoding='utf-8'
)

# Configuração do arquivo de log
formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')
handler.setFormatter(formatter)

# Adiciona o handler ao logger
logger.addHandler(handler)

# Configuração do handler para o terminal (Console)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter('%(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)

# Adiciona o handler de console ao logger
logger.addHandler(console_handler)

#---------------------------------------------------------------------------------

#---- Configurações do SFTP ----

hostname = ''
# Porta padrão para SFTP
port =  ''
username = ''
password = ''

#-------------------------------

#-------------------- Caminhos onde esta o arquivo ----------------------

local_file_path = r''  #não esquecer de adicoinar ao final do caminho onde o arquivo esta o nome do arquivo e a extensão dele
#caminho dentro sftp/nome do arquivo não esquecer a extensão ex: SFTP.csv
remote_file_path = r'caminho/dentro/do/sftp/nomedoarquivo.csv'  

#------------------------------------------------------------------------

class Carga_SFTP:
    def carregamento(self):
    
        # Conectando ao servidor SFTP
        try:
            if not os.path.exists(local_file_path):
                logging.info(f"Erro: O arquivo '{local_file_path}' não foi encontrado.")
            else:
                logging.info("O arquivo existe, continuando com o upload.")
                # Inicializando o cliente SSH
                transport = paramiko.Transport((hostname, port))
                transport.connect(username=username, password=password)

                # Inicializando o cliente SFTP
                sftp = paramiko.SFTPClient.from_transport(transport)
                logging.info("> Conectado com sucesso")
                logging.info("> Vamos iniciar o processo de carga")

                # Realizando o upload do arquivo
                sftp.put(local_file_path, remote_file_path)
                logging.info("Arquivo carregado com sucesso!")
        except Exception as e:
            logging.error(f"Erro ao realizar o upload: {e}")
        finally:
            # Fechando a conexão
            try:
                if sftp:
                    sftp.close()
                if transport:
                    transport.close()
            except NameError:
                # Ignora erros se sftp ou transport não foram inicializados
                pass
def main():
    start = Carga_SFTP()
    start.carregamento()
 
if __name__=='__main__':
    main()
