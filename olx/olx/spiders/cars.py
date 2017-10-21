# -*- coding: utf-8 -*-
import scrapy


class CarsSpider(scrapy.Spider):

    name = 'cars'
    allowed_domains = ['pe.olx.com.br']
    start_urls = ['http://pe.olx.com.br/veiculos-e-acessorios/carros']


    def parse(self, response):
        self.log('================================= CABEÇALHO - INÍCIO ======================================')
        self.log('Visitei página: %s' % response.url)
        self.log('=================================== CABEÇALHO - FIM ========================================')

        title_site = response.xpath('//title/text()').extract_first()
        self.log('================================= CABEÇALHO - INÍCIO ======================================')
        self.log('Cujo seu título é: %s' % title_site)
        self.log('=================================== CABEÇALHO - FIM ========================================')

        items = response.xpath(
            '//ul[@id="main-ad-list"]/li[not(contains(@class, "list_native"))]'
        )
        self.log('================================= CABEÇALHO - INÍCIO ======================================')
        self.log('=============== VISUALIZANDO TODOS OS ANÚNCIOS DE CARROS  ===============')
        self.log('QUANTIDADE DE ANÚNCIOS POR PÁGINA: %s'% len(items))
        self.log('=================================== CABEÇALHO - FIM ========================================')
        for item in items:
            url = item.xpath('./a/@href').extract_first()
            yield scrapy.Request(url=url, callback=self.parse_detail)
        next_page = response.xpath(
            '//div[contains(@class, "module_pagination")]//a[@rel = "next"]/@href'
        )
        if next_page:
            self.log('Próxima Página: {}'.format(next_page.extract_first()))
            yield scrapy.Request(
                url=next_page.extract_first(), callback=self.parse
            )

    def parse_detail(self, response):
        title = response.xpath('//title/text()').extract_first()

        year = response.xpath(
            '//span[contains(text(), "Ano")]/following-sibling::strong/a/@title'
            ).extract_first()

        ports = response.xpath(
            '//span[contains(text(), "Portas")]/following-sibling::strong/text()'
            ).extract_first()

        fuel = response.xpath(
            "//span[contains(text(), 'Combustível')]/following-sibling::strong/a/@title"
            ).extract_first()

        mileage = response.xpath(
            "//span[contains(text(), 'Quilometragem')]/following-sibling::strong/text()"
            ).extract_first()

        exchange = response.xpath(
            "//span[contains(text(), 'Câmbio')]/following-sibling::strong/text()"
            ).extract_first()

        county = response.xpath(
            "//span[contains(text(), 'Município')]/following-sibling::strong/a/@title"
            ).extract_first()

        # zipcode = response.xpath(
        #     "//span[contains(text(), 'CEP')]/following-sibling::strong/text()"
        #     ).extract_first()
        #
        # neighborhood = response.xpath(
        #     "//span[contains(text(), 'Bairro')]/following-sibling::strong//text()"
        #     ).extract_first()

        self.log('=============== VISUALIZANDO DETALHES DO CARRO  ===============')
        yield {

            'title': title,
            'year': year,
            'ports': ports,
            'fuel': fuel,
            'mileage': mileage,
            'exchange': exchange,
            'county': county,
            # 'zipcode': zipcode,
            # 'neighborhood': neighborhood,
        }
