from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup
from scrapy.crawler import CrawlerProcess


class Noticias(Item):
    titulo = Field()
    descripcion = Field()


class ElUniversoSpider(Spider):
    name = "SpiderUniverso"
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36'
    }

    start_urls = ["https://www.eluniverso.com/deportes"]

    # NOTE: PARSEAR EL ARBOL CON SCRAPY
    # def parse(self, response):
    #     sel = Selector(response)
    #     noticias = sel.xpath(
    #         '//div[@class="card-content | space-y-1 "]')
    #     # summary

    #     for noticia in noticias:
    #         item = ItemLoader(Noticias(), noticia)
    #         item.add_xpath('titulo','.//h2/a/text()')
    #         item.add_xpath('descripcion','.//p/text()')
    #         # itemp = item.get_xpath('./p/text()')
    #         # if len(itemp) != 0:
    #         #     print(item.get_xpath('./h2/a/text()'))
    #         #     print(item.get_xpath('./p/text()'))

    #         # print(item.get_xpath('./p/text()'))
    #         yield item.load_item()

    # NOTE:PARSEAR EL ARBOL CON BETUFLYSOUP
    def parse(self, response):
        soup = BeautifulSoup(response.body)
        contenedor_noticia = soup.find_all(
            'div', class_='card-content | space-y-1')

        for contenedor in contenedor_noticia:
            item = ItemLoader(Noticias(), response.body)
            titular = contenedor.h2('a')[0].text
            descripcion = contenedor.p
            if (descripcion != None):
                descripcion = descripcion.text
            else:
                descripcion = 'N/A'
            item.add_value('titulo', titular)
            item.add_value('descripcion', descripcion)
            yield item.load_item()


process = CrawlerProcess({
    'FEED_FORMAT': 'csv',
    'FEED_URI': 'resultados.csv'
})
process.crawl(ElUniversoSpider)
process.start()
