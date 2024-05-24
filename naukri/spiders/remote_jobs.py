import scrapy
import json

from scrapy.loader import ItemLoader

from naukri.items import JobItem


class RemoteJobsSpider(scrapy.Spider):
    name = "remote_jobs"
    allowed_domains = ["naukri.com"]
    start_urls = ["https://www.naukri.com/jobapi/v3/search?noOfResults="
                  "20&urlType=search_by_keyword&searchType=adv&keyword="
                  "remote&pageNo=1&seoKey=remote-jobs&src=discovery_"
                  "trendingWdgt_homepage_srch&latLong=31.046051_34.851612"]

    def parse(self, response, **kwargs):
        payload = json.loads(response.body)

        for job in payload['jobDetails']:
            i = ItemLoader(item=JobItem(), response=response)
            i.add_value('title', job['title'])
            i.add_value('company', job['companyName'])
            i.add_value('description', job['jobDescription'])
            i.add_value(
                'location',
                [x['label'] for x in job['placeholders']
                 if x['type'] == 'location']
            )
            i.add_value('date', job['createdDate'])

            yield i.load_item()
