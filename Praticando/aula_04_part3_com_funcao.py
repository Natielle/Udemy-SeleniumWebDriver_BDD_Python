
# Acessando site em localhost
# Locators organizados
# Utilização do teste através de função

# -------------------------------------------------------------
# Passo 1: Importar a biblioteca do Selenium
# -------------------------------------------------------------

# Selecionar "webdriver" e apertar F12 mostra a declaração do método
from selenium import webdriver
from selenium.webdriver.common.by import By  # Para utilizar o método find_element (é melhor para trabalhar com Page Objects)


# -------------------------------------------------------------
# Passo 2: Instanciar o driver que vai usar
# -------------------------------------------------------------

# Colocar o webdriver de cada navegador dentro das pastas C:\Users\wilbe\AppData\Local\Programs\Python\Python37\Scripts
# Ou o geckodriver precisa estar no PATH do SO.
driver = webdriver.Chrome()  # Apenas abre o driver(navegador) sem nada

# Organizando os locators
NOME = (By.ID, "name123")
PASS = (By.CLASS_NAME, "pass123")
SUBMIT = (By.CSS_SELECTOR, "button[class='form_submit'][type='submit']")
RESULT = (By.CSS_SELECTOR, "div.w3-border")


# -------------------------------------------------------------
# Passo 3: Abrindo um site em localhost (que não está online)
# -------------------------------------------------------------
# Comando que inicializa o servidor python:
# python -m http.server --bind 127.0.0.1 8083
# Faz referência para http://localhost:8083/html/login.html
# É obrigatório sempre colocar o http:// antes da url
driver.get("http://localhost:8083/S8-html/login.html")  # Visita a página do google pelo driver


# -------------------------------------------------------------
# Passo 4 e 5: Procurar o elemento que queremos manipular e aplicar ação
# -------------------------------------------------------------

# Deixando as ações em uma funcao
def login(user, password):
    # Encontrando os elementos
    elem01 = driver.find_element(*NOME)
    elem02 = driver.find_element(*PASS)
    elem03 = driver.find_element(*SUBMIT)

    # Realizando as acoes sobre os elementos
    elem01.send_keys(user)
    elem02.send_keys(password)
    elem03.click()

    elem04 = driver.find_element(*RESULT)
    elem04 = elem04.text

    # -------------------------------------------------------------
    # Passo 6: Validação da ação
    # -------------------------------------------------------------
    # É boa prática realizar comparações com letras minúsculas ou maiúculas apenas
    assert "uname=natielle&psw=minhasenha" in elem04.lower()  # Deixa o texto em minúscula antes da comparação

# Executa a funcao
login("Nadielle", "teste1234")

driver.quit()  # Fecha o navegador

# Para executar o script com o pyCharm basta apertar CTRL+SHIFT+F10






