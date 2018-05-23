# -*- coding: utf-8 -*-
import json

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class WikiPipeline(object):
    def open_spider(self, spider):
        self.file = open('data.json', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
	d = dict(item)
	self.file.write('{}\n'.format(str(d)))
	return item
