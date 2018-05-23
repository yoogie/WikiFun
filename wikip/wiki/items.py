# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WikiItem(scrapy.Item):
	url = scrapy.Field()
	title = scrapy.Field()
	desc  = scrapy.Field()
	links = scrapy.Field()
	footer = scrapy.Field()
#	last_changed = scrapy.Field() #candidate for LS-mutate from fotter?
