from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from os import getenv, environ

"""
Baixar a versao do chrome canary, no link abaixo.
https://www.google.com/chrome/browser/canary.html
"""

# 1. Instanciar o ChromeOptions, depois passa a localização do binario do chrome.
# 2. Depois adicionar o argumento headless e disable-gpu.
# 3. Passar o options como argumento no chromedriver.

options = webdriver.ChromeOptions()
path = getenv("LOCALAPPDATA")
options.binary_location = path_full = path + r"\Google\Chrome SxS\Application\chrome.exe"
print(path_full)
options._arguments = ['headless', 'disable-gpu']

driver = webdriver.Chrome(chrome_options=options)

# Abre a url.
driver.get("http://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_node_firstchild")
# Espera de forma implicita os elementos carregar na pagina.
driver.implicitly_wait(30)
# Muda para o frame correto.
driver.switch_to.frame("iframeResult")


def find(driver, selector, delay=30):
    return WebDriverWait(driver, delay).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, selector)))

elemento = find(driver, "#myList")

# innerHTML vai pegar o que estah contido dentro do elemento id=myList
# <ul id="myList"><li>Coffee</li><li>Tea</li></ul>
print(elemento.get_attribute('innerText'))

# Meus asserts pra saber se o teste foi realizado com sucesso.
assert "Coffee" in elemento.get_attribute('innerText')
assert "Tea" in elemento.get_attribute('innerHTML')

# fecha o browser
driver.quit()
