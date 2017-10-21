# python-scrapy-olx
Projeto de scraping com python

![Screenshot][1]

[1]:https://github.com/alisonamerico/python-scrapy-olx/blob/master/olx/olx/img/scrapy_python.jpg


## Instalação

1. Faça o clone do projeto:

```bash
$ git clone https://github.com/alisonamerico/python-scrapy-olx.git
```

2. Crie um ambiente virtualizado com [virtualenv]() e ative-o:

```bash
$ cd python-scrapy-olx
$ python3 -m venv .venv
$ source .venv/bin/activate
```

3. Executando o último comando, deve aparecer dessa forma:

```bash
(.venv)$
```

4. Isso significa que o ambiente foi ativado com sucesso. Agora vamos instalar as dependências:

```bash
(.venv)$ pip install -r requirements.txt
```

5. acesse a pasta olx:

```bash
(.venv)$ cd olx
```

6. Execute o crawl:

```bash
(.venv)$ scrapy crawl cars
```

Obs.: Caso queira ver o crawl com mais detalhe baixe a ide Studio 3T(https://studio3t.com/download/)

## Dúvidas ou problemas

Em caso de dúvidas ou problemas para configurar e rodar o projeto, crie uma [Issue](https://github.com/alisonamerico/python-scrapy-olx/issues) nesse repositório.
