import scrapy

from idealista.items import SellItem


class Core(scrapy.Spider):
    default_url = 'https://www.idealista.com'

    def __init__(self, name, action, item_type):
        super(Core, self).__init__()

        self.action = action
        self.item_type = item_type
        self.location = name

    def start_requests(self):
        urls = ['https://www.idealista.com/' + self.action + '-' + self.item_type + '/' + self.location + '/']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        flat_list = response.xpath('//div[@class="item-info-container"]')
        for flat in flat_list:
            title = flat.xpath('./a/text()').extract()

            link = self.default_url + flat.xpath('./a/@href').extract_first()

            price = flat.xpath('./div[@class="row price-row clearfix"]/span[@class="item-price"]/text()') \
                .extract_first(default='0').replace('.', '')

            drop_price = flat.xpath(
                './div[@class="row price-row clearfix"]/span[contains(@class, "item-price-down")]/text()') \
                .extract_first(default='0').strip().split(' ')[0].replace('.', '')

            rooms = int(flat.xpath("span[@class='item-detail']/small[contains(text(),'hab.')]/../text()")
                        .extract().pop().strip())

            m2 = float(flat.xpath('span[@class="item-detail"]/small[starts-with(text(),"m")]/../text()')
                       .extract().pop().replace('.', '').strip())

            flat_item = SellItem(
                title=title,
                link=link,
                price=price,
                drop_price=drop_price,
                rooms=rooms,
                m2=m2
            )

            # Go inside announcement and get more info
            request = scrapy.Request(response.urljoin(link), callback=self.parse_flat_details)
            request.meta['flat_item'] = flat_item

            yield request

        # Keep going to next page
        next_page = response.xpath('//div[@class="pagination"]//a[@class="icon-arrow-right-after"]/@href') \
            .extract_first()

        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_flat_details(self, response):
        flat_item = response.meta['flat_item']

        details_info = response.xpath('//section[@id="details"]')
        description = details_info.xpath(
            './div[@class="commentsContainer"]//div[@class="adCommentsLanguage expandable"]/text()').extract_first()

        price_details = details_info.xpath('./div[@class="details-block clearfix"]/div/div')
        price_per_m2 = price_details.xpath('./p[contains(., "/m")]/text()').extract_first()
        costs_per_month = price_details.xpath('./p[contains(., "/mes")]/text()').extract_first()

        address = '\n'.join(response.xpath('//div[@id="mapWrapper"]//div[@id="addressPromo"]/ul/li/text()').extract())
        addons = details_info.xpath('//ul/li[string-length(text()) > 1]/text()').extract()

        flat_item['description'] = description
        flat_item['price_per_m2'] = price_per_m2
        flat_item['costs_per_month'] = costs_per_month
        flat_item['address'] = address
        flat_item['addons'] = addons

        yield flat_item
