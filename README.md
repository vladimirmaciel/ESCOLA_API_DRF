# Formação Django Rest Framework - Alura

### Instalação do projeto: 

1. Baixe o projeto,
2. Crie um arquivo .venv e ative o ambiente

   ```
   python3.7 -m venv .venv
   source .venv/bin/activate

   ```
3. Instale o arquivo requirements.txt, contem as lib necessárias

   ```
   pip install -r requirements.txt
   ```
4. Execute o comando makemigrations e  migrate

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Criar um super usuário

   ```
   python manage.py createsuperuser 
   ```
