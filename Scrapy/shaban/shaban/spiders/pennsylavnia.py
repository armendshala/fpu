# -*- coding: utf-8 -*-
import re
import scrapy


class PennsylavniaSpider(scrapy.Spider):
    name = "pennsylavnia"
    allowed_domains = ["corporations.pa.gov"]
    start_urls = ['https://www.corporations.pa.gov/Search/CorpSearch']

    def parse(self, response):
        if response.status == 200:

            yield scrapy.FormRequest.from_response(
                response=response,
                formid='form1',
                formdata={
                    'ctl00$MainContent$txtSearchTerms':'AA',
                },
                dont_click=False,
                callback=self.parse1,
            )

    def parse1(self,response):
        if response.status == 200:
            lista = set(re.findall(r'Results\$ctl(\d+)',response.body,re.I|re.S))
            for i in lista:
                eventtarget = 'ctl00$MainContent$gvResults$ctl{0}$lnkBEName'.format(i)
                yield scrapy.FormRequest.from_response(
                    response=response,
                    formdata={
                        '__EVENTTARGET': eventtarget,
                    },
                    dont_click=True,
                    callback=self.parse2,
                )

    def parse2(self,response):
        if response.status == 200: pass
