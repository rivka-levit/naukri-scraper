import scrapy


class JobItem(scrapy.Item):
    title = scrapy.Field()
    company = scrapy.Field()
    description = scrapy.Field()
    location = scrapy.Field()
    date = scrapy.Field()
