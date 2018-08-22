# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#from questions.models import Questions
from myapp.models import Questions


class SpPipeline(object):
    def process_item(self, item, spider):
        return item


class ScrapyProjectPipeline(object):
    def process_item(self, item, spider):

        question = Questions()
        question.identifier = item["identifier"]
        question.title = item["title"]
        question.url = item["url"]
        question.save()
        return item
