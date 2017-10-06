# -*- coding: utf-8 -*-
import scrapy


class CarsSpider(scrapy.Spider):

    name = 'cars'
    allowed_domains = ['pe.olx.com.br']
    start_urls = ['http://pe.olx.com.br/']


    def parse(self, response):

        self.log('================================= CABEÇALHO - INÍCIO ======================================')
        self.log('VISITEI O SITE: %s' % response.url)
        self.log('=================================== CABEÇALHO - FIM ========================================')

        title_site = response.xpath('//title/text()').extract_first()
        self.log('================================= CABEÇALHO - INÍCIO ======================================')
        self.log('Cujo seu título é: %s' % title_site)
        self.log('=================================== CABEÇALHO - FIM ========================================')
        title_categories = response.xpath(
            '//h1[contains(@class, "search-category-title")]/text()'
            ).extract_first()
        categories = response.xpath(
            '//*[contains(@class, "search-category-nav")]//li/a/@href'
            )
        self.log('================================= CABEÇALHO - INÍCIO ======================================')
        self.log('Visualizando as categorias do site: %s' % categories)
        self.log('=================================== CABEÇALHO - FIM ========================================')
        for category in categories:
            url = category.xpath('.//a/@href').extract_first()
            yield scrapy.Request(
                url="http://pe.olx.com.br/veiculos-e-acessorios", callback=self.parse_sub_categories
            )

    def parse_sub_categories(self, response):
        title_sub_categories = response.xpath(
            '//h1[contains(@class, "title")]/text()'
            ).extract_first()
        sub_categories = response.xpath(
            '//*[contains(@class, "search-subcategory-nav")]//li/a/@href'
            )
        self.log('================================= CABEÇALHO - INÍCIO ======================================')
        self.log('Visualizando as sub categorias do site: %s' % sub_categories)
        self.log('=================================== CABEÇALHO - FIM ========================================')
        for sub_category in sub_categories:
            url = sub_category.xpath('.//a/@href').extract_first()
            yield scrapy.Request(
                url="http://pe.olx.com.br/veiculos-e-acessorios/carros", callback=self.parse_list_cars
            )

    def parse_list_cars(self, response):
        items = response.xpath(
            '//ul[@id="main-ad-list"]/li[not(contains(@class, "list_native"))]'
            )
        self.log('================================= CABEÇALHO - INÍCIO ======================================')
        self.log('VISITEI O SITE: %s' % response.url)
        self.log('=============== VISUALIZANDO TODOS OS ANÚNCIOS DE CARROS  ===============')
        self.log('QUANTIDADE DE ANÚNCIOS POR PÁGINA: %s'% len(items))
        self.log('=================================== CABEÇALHO - FIM ========================================')
        for item in items:
            url = item.xpath('./a/@href').extract_first()
            yield scrapy.Request(url=url, callback=self.cars_detail)
        next_page = response.xpath(
            '//div[contains(@class, "module_pagination")]//a[@rel = "next"]/@href'
        )
        if next_page:
            self.log('Próxima Página: {}'.format(next_page.extract_first()))
            yield scrapy.Request(
                url=next_page.extract_first(), callback=self.parse_list_cars
            )

    def cars_detail(self, response):
        title = response.xpath('//title/text()').extract_first()

        years = response.xpath(
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
            'years': years,
            'ports': ports,
            'fuel': fuel,
            'mileage': mileage,
            'exchange': exchange,
            'county': county,
            # 'zipcode': zipcode,
            # 'neighborhood': neighborhood,
        }
