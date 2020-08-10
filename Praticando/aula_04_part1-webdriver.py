
# Acessando site em localhost

# -------------------------------------------------------------
# Passo 1: Importar a biblioteca do Selenium
# -------------------------------------------------------------

# Selecionar "webdriver" e apertar F12 mostra a declaração do método
from selenium import webdriver


# -------------------------------------------------------------
# Passo 2: Instanciar o driver que vai usar
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


# -------------------------------------------------------------
# Passo 4 e 5: Procurar o elemento que queremos manipular e aplicar ação
# -------------------------------------------------------------

elem01 = driver.find_element_by_id("name123")
elem02 = driver.find_element_by_class_name("pass123")
elem03 = driver.find_element_by_css_selector("button[class='form_submit'][type='submit']")

# TEM DUAS MANEIRAS DE EXECUTAR AS ACOES SOBRE OS ELEMENTOS
# Maneira mais recomendada, pois é mais fácil a manutenção
elem01.send_keys("Natielle")
elem02.send_keys("minhasenha")
elem03.click()

# Maneira mais sucinta, mais difícil de debugar
# driver.find_element_by_id("name123").send_keys("Natielle")
# driver.find_element_by_class_name("pass123").send_keys("minhasenha")
# driver.find_element_by_css_selector("button[class='form_submit'][type='submit']").click()

elem04 = driver.find_element_by_css_selector("div.w3-border")
elem04 = elem04.text

# -------------------------------------------------------------
# Passo 6: Validação da ação
# -------------------------------------------------------------

# É boa prática realizar comparações com letras minúsculas ou maiúculas apenas
assert "uname=natielle&psw=minhasenha" in elem04.lower()  # Deixa o texto em minúscula antes da comparação

driver.quit()  # Fecha o navegador

# Para executar o script com o pyCharm basta apertar CTRL+SHIFT+F10






