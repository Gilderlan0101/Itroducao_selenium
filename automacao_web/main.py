from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager  # para Firefox
from selenium.webdriver.firefox.service import Service  # que vai executar
from time import sleep
# Instalando o WebDriver para o navegador | Versão recente
service = Service(GeckoDriverManager().install())  # Verifica a versão do WebDriver

# Qual vai ser o navegador
navegador = webdriver.Firefox(service=service)

# Entrando em um site
navegador.get("https://pages.hashtagtreinamentos.com/inscricao-minicurso-python-automacao-org?origemurl=hashtag_yt_org_minipython_videoselenium&_gl=1*1pkkd11*_gcl_aw*R0NMLjE3MzI4MzEwNTMuQ2p3S0NBaUF4cUM2QmhCY0Vpd0FsWHA0NTlnU192eFZTYnBSdTd3SmNBdXdaS2tEUVl4NGNDWEhTRURKN3lLOVU5cHlWR0xJS1hsOVZSb0NrUmdRQXZEX0J3RQ..*_gcl_au*MTk5ODAwODIxOC4xNzI5NTAxMTIxLjE1NDUzMjkwNjkuMTczMzUxOTM3OS4xNzMzNTE5Mzc5")

# Prence campos do front end com dados
navegador.find_element('xpath', '/html/body/div[2]/div[1]/section/div[2]/div/div[2]/form/div[1]/div/div[1]/div/input').send_keys("Maria") # para encontra os elementos da pagina | como voce vai encontra o elemento e o elemento
sleep(1)
navegador.find_element('xpath', '/html/body/div[2]/div[1]/section/div[2]/div/div[2]/form/div[1]/div/div[2]/div/input').send_keys('usuario_exemplo@gmail.com')
sleep(1)
navegador.find_element('xpath', '/html/body/div[2]/div[1]/section/div[2]/div/div[2]/form/div[1]/div/div[3]/div/input').send_keys('11222333555')