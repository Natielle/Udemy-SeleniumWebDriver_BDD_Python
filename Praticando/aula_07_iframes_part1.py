
# Locators organizados
# Utilização do teste através da classe e suas funcoes
# com espera explicita
# Manipulando Iframes

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


class IframeSample:
    def __init__(self, driver):
        # -------------------------------------------------------------
        # Passo 2: Instanciar o driver que vai usar
        # -------------------------------------------------------------
        # Organizando os locators
        self.RUN = (By.ID, "run")
        self.EXPANDIR = (By.CSS_SELECTOR, "small a[href*=\"google\"")
        self.HOME = (By.ID, "home")

    # Funcao generica para encontrar elementos
    def find(self, *locator, timeout=10):
        # Verifica se o elemento é visivel e se ele está na DOM
        element = WebDriverWait(driver, timeout).until(visibility_of_element_located(*locator))
        return element

    def run(self):
        self.find(self.RUN).click()

    def expandir(self):
        self.find(self.EXPANDIR).click()

    def home(self):
        self.find(self.HOME).click()

    def validar(self, url):
        # -------------------------------------------------------------
        # Passo 6: Validação da ação
        # -------------------------------------------------------------

        # Verificando a url
        assert self.driver.current_url == url

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
driver.get("https://jsfiddle.net/4b58ah85/7/")  # Visita a página do google pelo driver

teste = IframeSample(driver)  # Instanciando a classe

# Executa a funcao através da classe
teste.run()
teste.expandir()
teste.home()

teste.validar("https://jsfiddle.net/")  # Valida se voltou para página inicial

# ESSA EXECUÇÃO DÁ PROBLEMA PORQUE NÃO MODIFICAMOS O IFRAME PARA DAR O CLIQUE EM EXPANDIR

driver.quit()  # Fecha o navegador

# Para executar o script com o pyCharm basta apertar CTRL+SHIFT+F10






