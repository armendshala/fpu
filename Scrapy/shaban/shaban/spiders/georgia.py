# -*- coding: utf-8 -*-
import re
import scrapy


class GeorgiaSpider(scrapy.Spider):
    def __init__(self):
        self.page_start = 1
        self.page_stop = 40

    name = "georgia"
    allowed_domains = ["gadch.mylicense.com"]
    start_urls = ['https://gadch.mylicense.com/verification/Search.aspx']

    def getloop(self, m):
        return range(self.page_start, self.page_stop + 1) if m else range(self.page_start + 2, self.page_stop + 2)

    def checkpages(self, content):
        pattern = re.search(r'l40&#39;,&#39;&#39;\)"><font color="White">\.\.\.<',content,re.I|re.S)
        if pattern:
            return True
        else:
            return False

    def parse(self, response):
        if response.status == 200:
            yield scrapy.FormRequest.from_response(
                response=response,
                formid='form1',
                formdata={
                    't_web_lookup__first_name': 'A',
                },
                dont_click=False,
                callback=self.parse1,
            )

    def parse1(self,response):
        if response.status == 200:

            page_ = self.checkpages(response.body)

            lista_id = self.getloop(page_)
            for k in lista_id:
                yield scrapy.FormRequest.from_response(
                    response = response,
                    formdata = {
                        '__EVENTTARGET': 'datagrid_results$_ctl44$_ctl{0}'.format(k),
                    },
                    dont_click = True,
                    dont_filter=True,
                    callback = self.parse2,
                )

                if k == len(lista_id):
                    yield scrapy.FormRequest.from_response(
                        response = response,
                        formdata = {
                            '__EVENTTARGET': 'datagrid_results$_ctl44$_ctl{0}'.format(k),
                        },
                        dont_click = True,
                        dont_filter=True,
                        callback = self.parse1,
                    )

    def parse2(self,response):
        if response.status == 200:

            with open('AA.html', 'ab') as a:
                a.write(response.body)