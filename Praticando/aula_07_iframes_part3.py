
# Locators organizados
# Utilização do teste através da classe e suas funcoes
# com espera explicita
# Manipulando Iframes através do index

# -------------------------------------------------------------
# Passo 1: Importar a biblioteca do Selenium
# -------------------------------------------------------------
# Selecionar "webdriver" e apertar F12 mostra a declaração do método
from selenium import webdriver
from selenium.webdriver.common.by import By  # Para utilizar o método find_element (é melhor para trabalhar com Page Objects)
from selenium.webdriver.support.ui import WebDriverWait  # Aguarda o elemento
from selenium.webdriver.common.keys import Keys  # Dá acesso as teclas do teclado

# Espera o elemento através de uma condição
from selenium.webdriver.support.expected_conditions import visibility_of_element_located


class IframeSample:
    def __init__(self, driver):
        # -------------------------------------------------------------
        # Passo 2: Instanciar o driver que vai usar
        # -------------------------------------------------------------
        # Organizando os locators
        self.RUN = (By.ID, "run")
        self.EXPANDIR = (By.CSS_SELECTOR, "small a[href*=\"google\"")
        self.HOME = (By.CSS_SELECTOR, "a[title=\"JSFiddle\"]")
        self.EMPTY = (By.CSS_SELECTOR, "a[href=\"/\"]")


    # Funcao generica para encontrar elementos
    def find(self, *locator, timeout=10):
        # Verifica se o elemento é visivel e se ele está na DOM
        element = WebDriverWait(driver, timeout).until(visibility_of_element_located(*locator))
        return element

    def run(self):
        self.find(self.RUN).click()

    def expandir(self):
        # Mudando de frame para dar o click no expandir
        driver.switch_to.frame(0)  # Muda de frame pelo seu index

        self.find(self.EXPANDIR).click()

    def home(self):
        driver.switch_to.window(driver.window_handles[0])  # Volta para a primeira aba
        # Apos clicar em expandir, é necessário voltar para o frame padrão
        driver.switch_to.default_content()
        self.find(self.HOME).send_keys(Keys.ENTER)  # simula o click sobre o elemento
        self.find(self.EMPTY).send_keys(Keys.ENTER)

    def validar(self, url):
        # -------------------------------------------------------------
        # Passo 6: Validação da ação
        # -------------------------------------------------------------

        # Verificando a url
        assert url in driver.current_url

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
teste.expandir()  # Vai abrir o maps numa nova aba
teste.home()

teste.validar("https://jsfiddle.net/")  # Valida se voltou para página inicial

driver.quit()  # Fecha o navegador

# Para executar o script com o pyCharm basta apertar CTRL+SHIFT+F10






