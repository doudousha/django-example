# -*- coding: utf-8 -*-
import scrapy
#
# from scrapy_project.items import QuestionItem
from sp.items import QuestionItem


class StackoverflowCrawler(scrapy.Spider):
    name = "stackoverflow"
    allowed_domains = ["stackoverflow.com"]
    start_urls = ['http://stackoverflow.com/questions/41905464/use-djangos-models-in-a-scrapy-project-in-the-pipeline']

    def parse(self, response):
        item = QuestionItem()
        item["title"] = response.xpath('//div[@id="question-header"]/h1/a/text()').extract()[0]
        item["identifier"] = response.url.split("/")[4]
        item["url"] = response.url

        print(item)
        return item
