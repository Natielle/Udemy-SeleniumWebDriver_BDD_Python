from selenium import webdriver
from time import sleep
"""
Autor: Reinaldo M R Junior
Udemy - Curso de Selenium - Aula sobre a classe Switch.
"""
# Instanciando o chrome driver.
driver = webdriver.Chrome()

# Abre a url.
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_link_target")

# Espera de forma implicita os elementos carregar na pagina.
driver.implicitly_wait(10)

# Muda para o frame correto.
driver.switch_to.frame("iframeResult")

test = driver.find_element("tag name", "a")
test.click()
sleep(5)

test = driver.find_element("tag name", "a")
test.click()
sleep(5)

# verificando quantas janelas existe.
for key, handle in enumerate(driver.window_handles):
    print(key, handle)

# Imprimindo a janela atual
print("Janela Atual: {}".format(driver.current_window_handle))

# Mudamos o foco da primeira janela para a segunda janela
# usando o identificado, podemos usar o nome da janela tambem.
driver.switch_to.window(driver.window_handles[1])

# Pra te certeza mostro o identificado da segunda janela.
print("Janela Atual New: {}".format(driver.current_window_handle))

sleep(2)
test = driver.find_element("css selector", ".w3-button.w3-theme.w3-hover-green.w3-hover-shadow")
test.click()

# Imprimindo a url atual.
print(driver.current_url)
