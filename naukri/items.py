import scrapy

from scrapy.loader.processors import MapCompose

from datetime import date


def date_out(d):
    """
    Convert timestamp to a human-readable date.

    Args:
        d (int): timestamp received from spider

    Returns:
        str: date in human-readable format
    """

    d = d / 1000  # Get rid of milliseconds

    return str(date.fromtimestamp(d))


class JobItem(scrapy.Item):
    title = scrapy.Field()
    company = scrapy.Field()
    description = scrapy.Field()
    location = scrapy.Field()
    date = scrapy.Field(output_processor=MapCompose(date_out))
