Automatização V3 - Teste Unitário

Requisitos:

-Verificar a versão do browser (Chrome) para download do Chromedriver
https://chromedriver.chromium.org/downloads

-Alterar a linha 22,23 e 24 com Login, senha e o caminho para o chromedriver baixado

l = '#login#'
p = '#senha#'
driver = webdriver.Chrome(executable_path='/home/wellington/Documentos/v3/automatiza/chromedriver')'

-Pip

sudo apt install python-pip

- Selenium webdriver

'pip install selenium'

-Instalar o faker

'pip install faker'
- Python a partir da versão 2.7

Como executar o script:

python "nomedoscript.py"



