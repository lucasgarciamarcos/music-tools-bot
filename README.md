Primeira coisa é rodar o comando para criar um ambiente virutal

python -m venv venv 

Segundo passo é entrar no ambiente criado

venv/scripts/Activate

Depois (quando nao for usar o app) se quiser sair do ambiente o comando é: deactivate

O proximo passo é baixar as dependencias

pip install -r requirements.txt

E por ultimo rodar o codigo

python main.py