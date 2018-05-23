from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from bs4 import BeautifulSoup
from wiki.items import WikiItem

import re
import json


class Spider(CrawlSpider):
	name = "wikip"
	allowed_domains = ["wikipedia.org"]

	start_urls = [
		"https://en.wikipedia.org/wiki/Main_Page"
	]

	rules = (
		Rule(LinkExtractor(allow="https://en\.wikipedia\.org/wiki/.+",
			deny = ["https://en\.wikipedia\.org/wiki/Wikipedia.*",
        	                "https://en\.wikipedia\.org/wiki/Main_Page",
                	        "https://en\.wikipedia\.org/wiki/Free_Content",
                        	"https://en\.wikipedia\.org/wiki/Talk.*",
	                        "https://en\.wikipedia\.org/wiki/Portal.*",
        	                "https://en\.wikipedia\.org/wiki/Special.*"]),
		callback='parse_wikipedia_page'),
	)


	def parse_wikipedia_page(self, response):
		print '->', response.url
		item = WikiItem()
		soup = BeautifulSoup(response.body)
		item['url'] = response.url
		item['title'] = soup.find('h1', {'id':'firstHeading'}).string
		item['desc'] = soup.find('div', {'id':'mw-content-text'}).find('p')

		links= set()
		for link in soup.find('div', {'id':'mw-content-text'}).find('p').findAll('a', attrs={'href': re.compile('^/wiki/')}):
			links.add('http://en.wikipedia.org{}'.format(link.get('href')))

		arr = []
		for l in links:
			arr.append(l)

		item['links'] = arr
		return item
