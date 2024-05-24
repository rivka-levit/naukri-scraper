import scrapy
import json

from scrapy.loader import ItemLoader

from naukri.items import JobItem

from math import ceil


class RemoteJobsSpider(scrapy.Spider):
    name = "remote_jobs"
    allowed_domains = ["naukri.com"]
    start_urls = ["https://www.naukri.com/jobapi/v3/search?noOfResults="
                  "20&urlType=search_by_keyword&searchType=adv&keyword="
                  "remote&pageNo=1&seoKey=remote-jobs&src=discovery_"
                  "trendingWdgt_homepage_srch&latLong=31.046051_34.851612"]
    page = 1

    def parse(self, response, **kwargs):
        payload = json.loads(response.body)

        total_jobs = payload['noOfJobs']
        pages_per_page = payload['queryParamMap']['noOfResults']
        page_qty = ceil(total_jobs / pages_per_page)

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

        while self.page <= page_qty:
            self.page += 1
            base_url = (f"https://www.naukri.com/jobapi/v3/search?noOfResults="
                        f"20&urlType=search_by_keyword&searchType=adv&keyword="
                        f"remote&pageNo={self.page}&seoKey=remote-jobs&src=discovery_"
                        f"trendingWdgt_homepage_srch&latLong=31.046051_34.851612")

            yield response.follow(base_url, callback=self.parse)
