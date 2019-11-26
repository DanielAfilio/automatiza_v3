Automatização V3 - Teste Unitário

Requisitos:

-Versão do chromedriver relacionada ao seu browser (Chrome)
https://chromedriver.chromium.org/downloads

-Alterar a linha 22,23 e 25 com Login, senha e o caminho para o chromedriver baixado

l = '#login#'
p = '#senha#'
driver = webdriver.Chrome(executable_path='/home/wellington/Documentos/v3/automatiza/chromedriver')'

- Python a partir da versão 2.7

- Selenium webdriver

'pip install selenium'

Como executar o script:

python "nomedoscript.py"



