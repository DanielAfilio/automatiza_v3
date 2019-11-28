# Automatização V3 - Teste Unitário

Script para rodar teste unitário no ambiente local/homolog

## Install

- Python 
```
sudo apt-get install python2.7
```

- Pip (instalação de pacotes python)
```
sudo apt install python-pip
```

- Selenium webdriver
```

pip install selenium
```

- Faker
```

pip install faker
```


## Configurando o ambiente

- Clone o repositório 

- Abra o arquivo "cadastra_anunciante.py" e insira o login e a senha da plataforma nas variáveis "l" e "p" (login e password) das linhas 22 e 23

```
l = '#login#'
p = '#senha#'
```

- Passe o caminho do executável do chromedriver na linha 24 (Pasta principal do projeto) referente a sua máquina local

```
driver = webdriver.Chrome(executable_path='/home/wellington/Documentos/v3/automatiza/chromedriver')'
```


## Como executar o script:

python "nomedoscript.py"


### Em caso de erro:

- Na pasta principal do projeto, temos um executável chamado "chromedriver"
- Caso o seu Google Chrome possua versão inferior a 78.0 um erro pode ser apresentado no terminal ao rodar o script:

```
 No caso de erros referentes ao Chromedriver, substituir o chromedriver existente na pasta principal do projeto pelo chromedriver correspondente a sua versão do Chrome no link abaixo
```
* [Versões do chromedriver](https://chromedriver.chromium.org/downloads
) - Caso o script não rode por causa da versão do Chrome, baixar no link anterior o chromedriver referente ao seu navegador Chrome.

## Considerações

* Na primeira execução o script pode travar pois será a primeira vez abrindo o browser. Apenas feche o browser e rode o script novamente no terminal
* Para acompanhar o status da execução dos testes deixe o terminal aberto pois o mesmo retorna sucesso/erro
* A url pode ser alterada de homolog/local na instância driver.get() no início do arquivo.


## Caso de erro com o DOCKER

* Possivel erro com o Docker pode ser gerado depois da instalaço do Python. Caso isso ocorra colocar no terminal:
> pip install requests
