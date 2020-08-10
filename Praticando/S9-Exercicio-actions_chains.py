from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains
import time


driver = webdriver.Chrome()
url = "http://www.w3schools.com/js/tryit.asp?filename=tryjs_imagemap"
driver.get(url)

# Locators
IMAGEM = (By.CSS_SELECTOR, "area")


driver.switch_to.frame("iframeResult")  # Entra no frame antes de encontrar o elemento
elementos = driver.find_elements_by_tag_name("area")
venus = elementos[2]

print(elementos)
for i in elementos:
    print(" href: " + elementos[i].get_attribute('alt'))

# Utilizando actions chains
actions = ActionChains(driver)
actions.click(venus).perform()

# Verificando se abriu a imagem
url2 = driver.current_url
assert "http://www.w3schools.com/js/venus.htm" == url2

time.sleep(5)
driver.close()

"""
# TERMINAR, TA CLICANDO NO SOL AO INVÉS DO VENUS



driver = webdriver.Chrome()
driver.maximize_window()

url = "http://www.w3schools.com/js/tryit.asp?filename=tryjs_imagemap"
driver.get(url)
driver.implicitly_wait(15)

driver.switch_to.frame("iframeResult")  # Entra no frame antes de encontrar o elemento

# Locators
imagem = driver.find_element_by_css_selector("img[alt=\"Planets\"]")
venus = driver.find_element_by_css_selector("img[alt=\"Planets\"]")

x = int(venus.location['x'])
y = int(venus.location['y'])

actions = ActionChains(driver)
actions.drag_and_drop_by_offset(imagem, x + 128, y + 10).perform()

time.sleep(5)

"""