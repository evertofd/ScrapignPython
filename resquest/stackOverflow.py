import requests
from bs4 import BeautifulSoup
import os

encabezado = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

url = "https://stackoverflow.com/questions"

respuesta = requests.get(url, headers=encabezado)
soup = BeautifulSoup(respuesta.text, 'html.parser')

contenedor_de_preguntas = soup.find(id="questions")
lista_de_preguntas = contenedor_de_preguntas.find_all(
    'div', class_="s-post-summary")
for pregunta in lista_de_preguntas:
    texto_pregunta = pregunta.find('h3').text
    descripcion_pregunta = pregunta.find(
        class_="s-post-summary--content-excerpt").text.replace('\n', '').replace('\r', '').strip()
    print(texto_pregunta)
    print(descripcion_pregunta)
