
# Acessando site em localhost
# Locators organizados
# Utilização do teste através da classe e suas funcoes
# COM ESPERA IMPLICITA

# -------------------------------------------------------------
# Passo 1: Importar a biblioteca do Selenium
# -------------------------------------------------------------
# Selecionar "webdriver" e apertar F12 mostra a declaração do método
from selenium import webdriver
from selenium.webdriver.common.by import By  # Para utilizar o método find_element (é melhor para trabalhar com Page Objects)
from selenium.webdriver.support.ui import WebDriverWait  # Para utilizar a espera


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


    # Deixando as ações em uma funcao
    def login(self, user, password):
        # -------------------------------------------------------------
        # Passo 4 e 5: Procurar o elemento que queremos manipular e aplicar ação
        # -------------------------------------------------------------

        # Encontrando os elementos
        elem01 = driver.find_element(*self.NOME)
        elem02 = driver.find_element(*self.PASS)
        elem03 = driver.find_element(*self.SUBMIT)

        # Realizando as acoes sobre os elementos
        elem01.send_keys(user)
        elem02.send_keys(password)
        elem03.click()

    def validar(self, valor):
        # -------------------------------------------------------------
        # Passo 6: Validação da ação
        # -------------------------------------------------------------
        # Encontra o elemento
        elem04 = driver.find_element(*self.RESULT)
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

# Só precisa ser utilizada uma vez na sessão, pois ao procurar qualquer elemento vai esperar até 25s
driver.implicitly_wait(25)  # Aguarda ATÉ 25 segundos (Nessa execução não tem diferença com as anteriores)

teste = LogIn(driver)  # Instanciando a classe

# Executa a funcao através da classe
teste.login("Nadielle", "teste1234")
teste.validar("uname=nadielle&psw=teste1234")


driver.quit()  # Fecha o navegador

# Para executar o script com o pyCharm basta apertar CTRL+SHIFT+F10






