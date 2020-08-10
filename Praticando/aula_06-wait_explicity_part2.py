
# Acessando site em localhost
# Locators organizados
# Utilização do teste através da classe e suas funcoes
# COM ESPERA EXPLICITA COM MAIS DETALHES

# -------------------------------------------------------------
# Passo 1: Importar a biblioteca do Selenium
# -------------------------------------------------------------
# Selecionar "webdriver" e apertar F12 mostra a declaração do método
from selenium import webdriver
from selenium.webdriver.common.by import By  # Para utilizar o método find_element (é melhor para trabalhar com Page Objects)
from selenium.webdriver.support.ui import WebDriverWait  # Aguarda o elemento

# Espera o elemento através de uma condição
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, \
    invisibility_of_element_located, title_contains, title_is


class LogIn:
    def __init__(self, driver):
        # -------------------------------------------------------------
        # Passo 2: Instanciar o driver que vai usar
        # -------------------------------------------------------------
        # Organizando os locators
        self.NOME = (By.ID, "name123")
        self.PASS = (By.CLASS_NAME, "pass123")
        self.SUBMIT = (By.CSS_SELECTOR, "button[class='form_submit'][type='submit']")
        self.RESULT = (By.CSS_SELECTOR, "div.w3-border")

    # Funcao generica para encontrar elementos
    def find(self, *locator, timeout=30):
        # Verifica se o elemento é visivel e se ele está na DOM
        element = WebDriverWait(driver, timeout).until(visibility_of_element_located(*locator))
        return element

    # Funcao generica que aguarda o elemento nao estar presente
    def find_not(self, *locator, timeout=30):
        # Verifica se o elemento é visivel e se ele está na DOM
        element = WebDriverWait(driver, timeout).until(invisibility_of_element_located(*locator))
        return element

    # Funcao generica para verificar se o titulo passado está contido no titulo original
    def title_contains(self, *locator, timeout=30):
        return WebDriverWait(driver, timeout).until(title_contains(*locator))

    # Funcao generica para verificar se o titulo passado está IGUAL ao titulo original
    def titulo_igual(self, *locator, timeout=30):
        return WebDriverWait(driver, timeout).until(title_is(*locator))

    # Deixando as ações em uma funcao
    def login(self, user, password):
        # -------------------------------------------------------------
        # Passo 4 e 5: Procurar o elemento que queremos manipular e aplicar ação
        # -------------------------------------------------------------

        # Encontrando os elementos
        elem01 = self.find(self.NOME)
        elem02 = self.find(self.PASS)
        elem03 = self.find(self.SUBMIT)

        # Realizando as acoes sobre os elementos
        elem01.send_keys(user)
        elem02.send_keys(password)
        elem03.click()

    def validar(self, titulo_pagina, valor):
        # -------------------------------------------------------------
        # Passo 6: Validação da ação
        # -------------------------------------------------------------
        # Verifica se o botão sumiu
        self.find_not(self.SUBMIT)  # O submit some tão rápido que nem dá pra perceber

        # Verifica o titulo da pagina esta contido no titulo original
        assert self.title_contains(titulo_pagina)

        # Verifica o titulo da pagina esta EXATAMENTE IGUAL ao titulo original
        assert self.titulo_igual(titulo_pagina)

        # Encontra o elemento
        elem04 = self.find(self.RESULT)
        elem04 = elem04.text

        # É boa prática realizar comparações com letras minúsculas ou maiúculas apenas
        assert valor in elem04.lower()  # Deixa o texto em minúscula antes da comparação

    # -------------------------------------------------------------
    # FIM DA CLASSE
    # -------------------------------------------------------------


# Colocar o webdriver de cada navegador dentro das pastas C:\Users\wilbe\AppData\Local\Programs\Python\Python37\Scripts
# Ou o geckodriver precisa estar no PATH do SO.
driver = webdriver.Chrome()  # Apenas abre o driver(navegador) sem nada

# -------------------------------------------------------------
# Passo 3: Abrindo um site em localhost (que não está online)
# -------------------------------------------------------------
# Comando que inicializa o servidor python:
# python -m http.server --bind 127.0.0.1 8083
# Faz referência para http://localhost:8083/html/login.html
# É obrigatório sempre colocar o http:// antes da url
driver.get("http://localhost:8083/S8-html/login.html")  # Visita a página do google pelo driver

teste = LogIn(driver)  # Instanciando a classe

# Executa a funcao através da classe
teste.login("Nadielle", "teste1234")

# teste.validar("Forms action page", "uname=nadielle&psw=teste1234")  # Passa nos dois asserts de titulo
teste.validar("Forms action", "uname=nadielle&psw=teste1234")  # Passa apenas no assert do titulo do contain

driver.quit()  # Fecha o navegador

# Para executar o script com o pyCharm basta apertar CTRL+SHIFT+F10






