import requests
import parsel
import string

session = requests.Session()

user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
session.headers.update({
    'user-agent':user_agent,
})

def change_proxy():
    proxy = ''
    session.proxies = {
        'http':proxy,
        'https': proxy,
    }

if __name__ == '__main__':

    for i in range(10):
    # for i in string.ascii_uppercase:
    # for i in range(65,92):
    #     i = chr(i)
        print 'Searching for id:',i
        while True:
            main_url = 'https://www.corporations.pa.gov/search/corpsearch'
            r =session.get(main_url)
            if r.status_code == 200:

                sel = parsel.Selector(text=r.text)

                response_post = session.post(
                    url='https://www.corporations.pa.gov/search/corpsearch',
                    data={
                        '__LASTFOCUS':'',
                        '__EVENTTARGET':'',
                        '__EVENTARGUMENT':'',
                        '__VIEWSTATE':sel.xpath('*//input[@id="__VIEWSTATE"]/@value').extract_first(),
                        '__VIEWSTATEGENERATOR':sel.xpath('*//input[@id="__VIEWSTATEGENERATOR"]/@value').extract_first(),
                        '__VIEWSTATEENCRYPTED':'',
                        '__EVENTVALIDATION':sel.xpath('*//input[@id="__EVENTVALIDATION"]/@value').extract_first(),
                        'ctl00$MainContent$txtSearchTerms':str(i),
                        'ctl00$MainContent$ddlSearchType':'1',
                        'ctl00$MainContent$btnSearch':'Search',
                    }
                )
                if response_post.status_code == 200:

                    sel = parsel.Selector(text=response_post.text)

                    response_company = session.post(
                        url='https://www.corporations.pa.gov/search/corpsearch',
                        data={
                            '__LASTFOCUS': '',
                            '__EVENTTARGET': 'ctl00$MainContent$gvResults$ctl02$lnkBEName',
                            '__EVENTARGUMENT': '',
                            '__VIEWSTATE': sel.xpath('*//input[@id="__VIEWSTATE"]/@value').extract_first(),
                            '__VIEWSTATEGENERATOR': sel.xpath(
                                '*//input[@id="__VIEWSTATEGENERATOR"]/@value').extract_first(),
                            '__VIEWSTATEENCRYPTED': '',
                            '__EVENTVALIDATION': sel.xpath('*//input[@id="__EVENTVALIDATION"]/@value').extract_first(),
                            'gvResults_length':'10'
                        }
                    )

                    if response_company.status_code == 200:
                        print response_company.status_code
                        break

                elif response_post.status_code == 503:
                    change_proxy()

