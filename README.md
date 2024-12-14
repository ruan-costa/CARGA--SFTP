# Upload de Arquivos para SFTP


[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/)

Bem-vindo ao projeto de upload de arquivos para um servidor SFTP! Este projeto utiliza a biblioteca `paramiko` para conectar-se ao servidor SFTP e realizar o carregamento de arquivos de forma automática.

## 🚀 Funcionalidades
- **Conexão ao Servidor SFTP**: Estabelece conexão segura com o servidor SFTP utilizando credenciais de login.
- **Upload de Arquivos**: Permite o upload de arquivos de um diretório local para o servidor SFTP, em uma pasta específica.
- **Gerenciamento de Logs**: Geração de logs detalhados, tanto na tela quanto em um arquivo, para acompanhamento do processo de upload.

## 🛠️ Instalação

### Pré-requisitos
- Python 3.10+
- Conta de acesso ao servidor SFTP com permissões adequadas
- Caminho do diretório local e do diretório remoto no servidor SFTP

### Instalar Dependências
Na pasta do projeto, execute o comando abaixo para instalar as dependências:
```bash
pip install paramiko

📋 Uso
Configurações Iniciais
Para usar este projeto, você precisará fornecer as seguintes informações:
Login e senha: Credenciais de acesso ao servidor SFTP.
Caminho Local: Caminho para o arquivo ou diretório local que será carregado.
Caminho Remoto: Caminho da pasta no servidor SFTP onde o arquivo será armazenado.


📂 Estrutura de Arquivos
.
├── CARGA_SFTP.py              # Script principal para conexão e upload no servidor SFTP
├── Log/                       # Pasta onde os arquivos de log serão salvos
├── README.md                  # Este arquivo README


📧 Contato
Se você tiver alguma dúvida, sinta-se à vontade para entrar em contato:

Telefone: (81) 98761-4812

Este projeto facilita o upload de arquivos para servidores SFTP, proporcionando um processo automatizado e eficiente! 🎉🚀