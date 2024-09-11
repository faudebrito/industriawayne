# Instalação do Sistema

Siga os passos abaixo para configurar o ambiente de desenvolvimento do sistema **Indústria Wayne**.

## 1. Clonar o Repositório

COMMAND PROMPT
git clone https://github.com/faudebrito/industriawayne

## 2. Crie um ambiente virtual para isolar as dependências do projeto.

python -m venv venv
source venv/bin/activate  # No Windows, use venv\Scripts\activate

## 3. Instale todas as dependências listadas no arquivo requirements.txt.

pip install -r requirements.txt

## 4. Configure o banco de dados e rode as migrações.

python manage.py makemigrations
python manage.py migrate

## 5. Inicie o servidor de desenvolvimento local.

python manage.py runserver

## 6. Agora você pode acessar o sistema em http://localhost:8000.



