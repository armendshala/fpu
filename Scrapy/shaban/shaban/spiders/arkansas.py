# -*- coding: utf-8 -*-
import re
import scrapy


class ArkansasSpider(scrapy.Spider):
    name = "arkansas"
    start_urls = ['http://www.sos.arkansas.gov/corps/search_all.php']

    def parse(self, response):
        if response.status == 200:

            # yield scrapy.FormRequest(
            #     url='http://www.sos.arkansas.gov/corps/search_corps.php',
            #     formdata={
            #         'corp_type_id': '',
            #         'corp_name': 'AA',
            #         'fict_name': '',
            #         'agent_search': '',
            #         'agent_city': '',
            #         'agent_state': '',
            #         'filing_number': '',
            #         'cmd': '',
            #         'SEARCH': 'Search',
            #     },
            #     dont_filter=True,
            #     callback=self.search_result,
            # )

            # yield scrapy.FormRequest.from_response(
            #     response=response,
            #     formnumber=0,
            #     formdata={
            #         'corp_name':'AA',
            #     },
            #     dont_click=False,
            #     callback=self.search_result,
            # )

            yield scrapy.FormRequest.from_response(
                response=response,
                formnumber=0,
                formdata={
                    'corp_type_id': 'b15',
                },
                dont_click=False,
                callback=self.search_result,
            )

    def search_result(self,response):
        if response.status == 200:

            for link in re.findall(r' href="(search_corps\.php\?DETAIL=[^"]+)">',response.body,re.I|re.S):
                link = response.urljoin(link)
                print link

                # yield scrapy.Request(link,callback=self.company)

            patt = re.search(r'<a href="([^"]+)">Next ',response.body,re.I|re.S)
            if patt:
                yield scrapy.Request(
                    url=response.urljoin(patt.group(1)),
                    dont_filter=True,
                    callback=self.search_result,
                )
            else:
                print 'DONE.'

    def company(self,response):
        if response.status == 200:
            pass
            # save to db