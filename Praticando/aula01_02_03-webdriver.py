
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
driver = webdriver.Firefox()  # Apenas abre o driver(navegador) sem nada


# -------------------------------------------------------------
# Passo 3: Abrir a url do site
# -------------------------------------------------------------

# É obrigatório sempre colocar o http:// antes da url
driver.get("http://www.google.com")  # Visita a página do google pelo driver


# -------------------------------------------------------------
# Passo 4: Procurar o elemento que queremos manipular
# -------------------------------------------------------------

# Não funciona porque não existe este elemento na página
# element = driver.find_element_by_id("p")  # Encontra um elemento da página que tenho o id = "p"

# Para procurar o elemento de outra maneira podemos pesquisar pela tag
# element = driver.find_element_by_tag_name("input")  # Pode existir mais de um elemento
element = driver.find_element_by_tag_name("input[name=\"btnI\"]")  # Especifica que o elemento selecionado será o input que tem o name "btnI"


# -------------------------------------------------------------
# Passo 5: Aplicar ação sobre os elementos
# -------------------------------------------------------------

# Selecionar "text" e apertar F12 mostra a declaração do método
print(element.text)  # Mostra o texto do elemento encontrado (Neste caso não vai mostrar nada)

# Para que seja exibido o conteúdo de um elemento input, precisamos utilizar outra propriedade
print(element.get_attribute('value'))
value_button = element.get_attribute('value')

# -------------------------------------------------------------
# Passo 6: Validação da ação
# -------------------------------------------------------------

# É boa prática realizar comparações com letras minúsculas ou maiúculas apenas
assert "estou com sorte" == value_button.lower()  # Deixa o texto em minúscula antes da comparação

# Se o assert falhar, o teste para e não fecha o browser
# assert "estou com sorte 123" == value_button.lower()  # Faz o assert falhar, pois valores são diferentes
# assert "estou com sorte" == value_button  # Faz o assert falhar por conta da letra maiuscula


driver.quit()  # Fecha o navegador

# Para executar o script com o pyCharm basta apertar CTRL+SHIFT+F10






