import scrapy


class RemoteJobsSpider(scrapy.Spider):
    name = "remote_jobs"
    allowed_domains = ["naukri.com"]
    start_urls = ["https://www.naukri.com/remote-jobs"]

    def parse(self, response, **kwargs):
        pass
