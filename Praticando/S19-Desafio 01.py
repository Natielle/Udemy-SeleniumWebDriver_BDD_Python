from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep
import string

driver = webdriver.Chrome(executable_path="C:\\chromedriver")
url = "http://catamaranprojects.com/wordsearch/"
driver.get(url)

# Clica para comecar o jogo
botao_start = driver.find_element_by_css_selector("button[type='button']")
botao_start.click()

# encontrando os elementos da página
lista_palavras = driver.find_elements_by_css_selector(".col .span_3_of_12 .section .group")
vetor_letras = driver.find_elements_by_css_selector(".col .span_1_of_10")

# Auxliares
abc = list(string.ascii_lowercase)
ABC = list(string.ascii_uppercase)
lista_letras = []

# Percorre o caca palavras
for key, j in enumerate(vetor_letras):
        letra = vetor_letras[key].get_attribute('innerText')
        if letra == "":
            lista_letras.append(" ")
        else:
            lista_letras.append(letra)

print("Letras do caca palavras : {}".format(lista_letras))

# Cadeia de caracteres para procurar horizontalmente
str_letras_h = ''.join(lista_letras)
print(str_letras_h)

# Cadeia de caracteres para procurar verticalmente (FALTA FAZER)
# letras_vert =[]
# for i, x in enumerate(vetor_letras):
#     if str(i)[-1] in (str(range(2, 8))):
#         print("str(i)[-1]: {}".format(str(i)[-1]))
#         for mult in range(0, 60, 10):
#             print("mult:", mult)
#             print("i*mult: {}".format(i+mult))
#             letras_vert.append(vetor_letras[i+mult].get_attribute('innerText'))
#
# print("Coluna 1: {}".format(letras_vert))


for keys, i in enumerate(lista_palavras):
    palavra = lista_palavras[keys].get_attribute('innerText')
    print(palavra)

    index_p = str_letras_h.find(palavra)
    print("Posicao onde encontrou a palavra '{}': {}".format(palavra, index_p))

    # Se encontrou a palavra na horizontal
    if index_p != -1:
        end_p = index_p + len(palavra)
        print("max: {}".format(end_p))

        for y in range(index_p, end_p): # Clica nas letras
            print(y)
            vetor_letras[y].click()
            sleep(1)
        sleep(2)
    # else: # Precisa encontrar a palavra na vertical

sleep(5)

# driver.close()
