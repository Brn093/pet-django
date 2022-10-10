# § Informando qual interpretador será utilizado
    . Ctrl + Shift + P (Selecione o Interpretador gerado no ambiente virtual no VSCODE)

# § Criando um projeto no Django

    . django-admin startproject nome_do_projeto

# § Criando um app no Django

    . django-admin startapp nome_do_app

# § Iniciando o Django no Navegador

    . python manage.py runserver

# § Listando as versões das dependências instaladas

    . pip freeze
    . pip freeze > requirements.txt (caso queira passar as dependências para um arquivo de texto)

# § Criando as tabelas default no banco SqLite

    . python manage.py migrate

# § Criando um usuário para acesso ao sistema admin do django(obs.: Acesso apenas para administrador)

    . python manage.py createsuperuser

# § Preparando a migração dos dados 

    . python manage.py makemigrations nome_do_app
    . (depois para criar as tabelas) python manage.py migrate nome_do_app

# § Gerando o meu sql apenas

    . python manage.py sqlmigrate core 0001



