
# ATIVIDADE PROPOSTA PELO PROFESSOR DO CURSO

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
# Passo 3: Abrir a url do site
# -------------------------------------------------------------

# É obrigatório sempre colocar o http:// antes da url
driver.get("http://www.google.com")  # Visita a página do google pelo driver


# -------------------------------------------------------------
# Passo 4: Procurar o elemento que queremos manipular
# -------------------------------------------------------------

driver.set_page_load_timeout(10)
# element01 = driver.find_element_by_id("")  # Analisando a página do google, não tem elemento com id
element02 = driver. find_element_by_class_name("gNO89b")  # (possui tag input)
element03 = driver.find_element_by_css_selector("input[name=\"q\"]")  # input pesquisar (possui tag input)
element04 = driver.find_element_by_xpath("//*[@id=\"tsf\"]/div[2]/div/div[3]/center/input[1]") # botao pesquisar (possui tag input)
element05 = driver.find_element_by_name("btnK")  # botao pesquisar (possui tag input)
element06 = driver.find_element_by_link_text("Como funciona a Pesquisa")  # link
element07 = driver.find_element_by_partial_link_text("funciona a Pesquisa")  # link


# -------------------------------------------------------------
# Passo 5: Aplicar ação sobre os elementos
# -------------------------------------------------------------


print(driver.page_source)  # Mostra o código-fonte da página atual
print(driver.title)        # Mostra o título da página atual
print(driver.current_url + "\n")  # Mostra a url da página atual

print("Elemento 2: " + element02.get_attribute('value'))
print("Elemento 3: " + element03.get_attribute('value'))  # Nao vai aparecer nada
print("Elemento 4: " + element04.get_attribute('value'))
print("Elemento 5: " + element05.get_attribute('value'))
print("Elemento 6: " + element06.text)
print("Elemento 7: " + element07.text)

driver.quit()  # Fecha o navegador

# Para executar o script com o pyCharm basta apertar CTRL+SHIFT+F10






