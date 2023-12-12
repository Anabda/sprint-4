# Sobre o projeto
O projeto tem como objetivo predizer se um paciente possui problemas cardíacos a partir de dados de sua saúde. O que cada campo significa pode ser encontrado no arquivo Dataset Description.png.
O arquivo realizado no colab está dentro da pasta Dataset com o nome Dataset.ipynb

# Como executar


Instalar todas as libs python listadas no `requirements.txt`.
Copiar o repositório para uma pasta local e executar os comandos abaixo pelo terminal após entrar no diretório do repositório:

1- Criar uma virtualenv
```
virtualenv nome_da_virtualenv
```

2- Ativar a virtualenv
```
nome_da_virtualenv\Scripts\Activate
```

3- Instalar as bibliotecas do arquivo requirements.txt 
```
(env)$ pip install -r requirements.txt
```

4- Executar a API:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```
5- Após uma mudança no código fonte:

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

6 - Abrir o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.
