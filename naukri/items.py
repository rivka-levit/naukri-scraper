import scrapy

from scrapy.loader.processors import MapCompose, Join

from datetime import date
from w3lib.html import remove_tags


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
    title = scrapy.Field(output_processor=Join())
    company = scrapy.Field(output_processor=Join())
    description = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=Join()
    )
    location = scrapy.Field(output_processor=Join())
    data = scrapy.Field(output_processor=MapCompose(date_out))
