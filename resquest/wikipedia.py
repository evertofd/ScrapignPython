import requests
from lxml import html

encabezado = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

url = "https://www.wikipedia.org/"

respuesta = requests.get(url,headers=encabezado)

parser = html.fromstring(respuesta.text)

# ingles = parser.get_element_by_id("js-link-box-en")

# print(ingles.text_content())

# ingles = parser.xpath("//a[@id='js-link-box-en']/strong/text()")

alllenguajes = parser.xpath("//div[contains(@class,'central-featured-lang')]//strong/text()")
for lenguaje in alllenguajes:
    print(lenguaje)