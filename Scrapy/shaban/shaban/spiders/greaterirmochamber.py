# -*- coding: utf-8 -*-
import re
import scrapy
import string

from scrapy import Request

class GreaterirmochamberSpider(scrapy.Spider):
    name = "greaterirmochamber"

    start_urls = ['http://greaterirmochamber.chambermaster.com/list/']

    def start_requests(self):
        yield scrapy.Request('http://greaterirmochamber.chambermaster.com/list/searchalpha/0-9')

        for c in string.ascii_lowercase:
            yield scrapy.Request('http://greaterirmochamber.chambermaster.com/list/searchalpha/{0}'.format(c))

    def parse(self, response):
        for link in re.findall(r'<div class="mn-title" itemprop="name">\s*<a href="([^"]+)"',response.body,re.I|re.S):

            yield Request(
                url=link,
                method="GET",
                dont_filter=True,
                callback=self.response_company,
            )

        yield scrapy.Request(url='nextpage',method="GET",dont_filter=True,callback=self.parse,)

    def response_company(self,response):
        if response.status == 200:
            company_name = ''
            pattern_name = re.search(r'<h1 itemprop="name">([^<]+)</h1>',response.body,re.I|re.S)
            if pattern_name:
                company_name = pattern_name.group(1)

            yield {
                'Name':company_name
            }