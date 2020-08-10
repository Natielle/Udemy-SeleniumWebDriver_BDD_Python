
# Locators organizados
# Utilização do teste através da classe e suas funcoes
# com espera explicita
# Manipulando abas

from selenium import webdriver
from time import sleep

# instanciando o chrome
driver = webdriver.Chrome()

# Abrindo a url
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_link_target")

# Espera de forma implicita os elementos carregar na pagina.
driver.implicitly_wait(10)

# Muda para o frame correto.
driver.switch_to.frame("iframeResult")

# Procura o elemento no frame iframeResult
test = driver.find_element("tag name", "a")  # é um link
test.click()
sleep(5)

test = driver.find_element("tag name", "a")
test.click()
sleep(5)

# verificando quantas janelas existe. (Imprime todas as janelas abertas)
for key, handle in enumerate(driver.window_handles):  # enumera as janelas
    # handle é o identificador da janela dentro do contexto (cada vez que rodar o selenium é diferente)
    print(key, handle)

# Imprimindo a janela atual
print("Janela Atual: {}".format(driver.current_window_handle))  # Vai mostrar que está na 1° janela

# Mudamos o foco da primeira janela para a segunda janela
# usando o identificado, podemos usar o nome da janela tambem.
driver.switch_to.window(driver.window_handles[1])  # 0 -> 1° janela

# Pra te certeza mostro o identificado da segunda janela.
print("Janela Atual New: {}".format(driver.current_window_handle))

sleep(2)
test = driver.find_element("css selector", ".w3-button.w3-theme.w3-hover-green.w3-hover-shadow")
test.click()  # Dá o click na segunda página

# Imprimindo a url atual.
print(driver.current_url)