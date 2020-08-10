
# Acessando site em localhost
# Locators organizados
# Utilização do teste através da classe e suas funcoes
# COM ESPERA IMPLICITA

# -------------------------------------------------------------
# Passo 1: Importar a biblioteca do Selenium
# -------------------------------------------------------------
# Selecionar "webdriver" e apertar F12 mostra a declaração do método
from selenium import webdriver
import time # Biblioteca que tem funcoes relacionadas ao tempo


# Funcao que calcula o tempo esperado
def calculate_implicit_wait_time(driver, wait_value):

    # somente entre se tiver valor. (Se tiver algum valor de espera, há espera implicita)
    if wait_value:
        driver.implicitly_wait(wait_value)

    # dou o clique no elemento.
    driver.find_element_by_id("bt01").click()

    # função para pegar o tempo em segundos.
    now = time.time()

    try:
        myelement = driver.find_element_by_id("meuId")

    # caso der erro vai entrar na exceção e imprimir o erro.
    except Exception as x:
        print(x)

    # mostrando que é preciso aplicar somente uma vez.
    # fazendo o teste com o outro botão.
    driver.find_element_by_id("bt02").click()

    try:
        myelement = driver.find_element_by_id("meuId2")

    # caso der erro vai entrar na exceção e imprimir o erro.
    except Exception as x:
        print(x)

    # imprime a media do tempo.
    print(str(int(time.time()-now))+'--Seconds')


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
driver.get("http://localhost:8083/S8-html/wait.html")  # Visita a página wait em localhost

calculate_implicit_wait_time(driver, 25)  # Aguarda até 25 segundos para encontrar elementos da funcao

# Vai dar erro, pois os elementos só aparecem 15s depois do clique, e aqui espera até 10s.
# calculate_implicit_wait_time(driver, 10)  # Imprime as mensagens de exceção

driver.close()  # Fecha o navegador

# Para executar o script com o pyCharm basta apertar CTRL+SHIFT+F10







