import re
import requests
import pyodbc

import threading
from Queue import Queue

class ProfLicGeorgia(threading.Thread):
    def __init__(self,num,q,lock):
        threading.Thread.__init__(self)

        self.headers = {
            'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
        }
        self.s = requests.Session()
        self.s.headers.update(self.headers)
        self.page = 50

        self.inserted = [str(x).strip() for x in open('Ids.txt','r')]
        self.taskid = 1234

        self.num = num
        self.q = q
        self.lock = lock

    def getCategories(self):

        categories_list = list()

        response = self.s.get(
            'http://verify.sos.ga.gov/Verification/Search.aspx'
        )
        if response.status_code == 200:

            snippet1 = re.search(r'<span id="lab_Profession">(.*?)</select>', response.content, re.I | re.S)
            if snippet1:

                for category in re.findall(r'value="([^"]+)"', snippet1.group(1), re.I | re.S):
                    category = category.replace('&amp;', '&')
                    categories_list.append(category)

        return categories_list

    def getNextpage(self,response):
        return_response = None
        if response.status_code == 200:
            nextpage = 'datagrid_results$_ctl44$_ctl'
            response_nextPage = self.s.post(
                url='http://verify.sos.ga.gov/Verification/SearchResults.aspx',
                data={
                    'CurrentPageIndex':self.page,
                    '__EVENTTARGET':nextpage,
                    '__EVENTARGUMENT':'',
                    '__VIEWSTATE':re.search(r'id="__VIEWSTATE" value="([^"]+)"',response.content,re.I|re.S).group(1),
                    '__VIEWSTATEGENERATOR':re.search(r'id="__VIEWSTATEGENERATOR" value="([^"]+)"',response.content,re.I|re.S).group(1),
                    '__EVENTVALIDATION':re.search(r'id="__EVENTVALIDATION" value="([^"]+)"',response.content,re.I|re.S).group(1),
                },
            )
            if response_nextPage.status_code == 200:
                return_response = response_nextPage
                #self.checkIfLastPage(response_nextPage)
                self.page += 1
                print 'Page: %s' % self.page

        return return_response

    def savetodb(self,pagelink,content,id):
        try:
            cnxn = pyodbc.connect(
                'DRIVER={SQL Server};SERVER=serverdell\serverdell;DATABASE=Downpage_Base;UID=downuser;Pwd=downuser;')
            cursor = cnxn.cursor()
            cursor.execute("insert into com_request1 (pagelink,webreq,sourceID) values(?,?,?)", (pagelink, content, id))
            cnxn.commit()
            cnxn.close()
            return True
        except Exception as e:
            print(e)
            return False

    def saveLinks(self,link):
        with open('Ids.txt','ab') as a:
            a.write(link + '\n')
            self.inserted.append(link)

    def getLinks(self,content):
        if content:

            for link in re.findall(r'href="Details\.aspx\?result=([^"]+)"', content,
                                   re.I | re.S):
                url = 'http://verify.sos.ga.gov/Verification/Details.aspx?result=%s' % link
                response_company = self.s.get(url)
                if response_company.status_code == 200:
                    content = response_company.content

                    patt_lic = re.search(r'ctl34__ctl1_license_no" maxlength="50">([^<]+)<',response_company.content,re.I|re.S)
                    if patt_lic:

                        self.saveLinks(patt_lic.group(1))
                        # self.savetodb(url,content,self.taskid)
                        print 'Thread: %s - Inserted: %s' % (self.num,patt_lic.group(1))

    def run(self):

        while self.q.qsize() > 0:

            self.lock.acquire()
            category = self.q.get()
            print 'Category: %s' % category
            self.lock.release()

            response = self.s.get('http://verify.sos.ga.gov/Verification/Search.aspx')
            if response.status_code == 200:

                data = {
                    '__EVENTTARGET':'t_web_lookup__profession_name',
                    '__EVENTARGUMENT':'',
                    '__LASTFOCUS':'',
                    '__VIEWSTATE':re.search(r'id="__VIEWSTATE" value="([^"]+)"',response.content,re.I|re.S).group(1),
                    '__VIEWSTATEGENERATOR':re.search(r'id="__VIEWSTATEGENERATOR" value="([^"]+)"',response.content,re.I|re.S).group(1),
                    '__EVENTVALIDATION':re.search(r'id="__EVENTVALIDATION" value="([^"]+)"',response.content,re.I|re.S).group(1),
                    't_web_lookup__profession_name':category,
                    't_web_lookup__first_name':'',
                    't_web_lookup__license_type_name':'',
                    't_web_lookup__last_name':'',
                    't_web_lookup__license_no':'',
                }

            response_category = self.s.post('http://verify.sos.ga.gov/Verification/Search.aspx',data)
            if response_category.status_code == 200:

                data = {
                    '__EVENTTARGET': '',
                    '__EVENTARGUMENT': '',
                    '__LASTFOCUS': '',
                    '__VIEWSTATE': re.search(r'id="__VIEWSTATE" value="([^"]+)"', response_category.content, re.I | re.S).group(
                        1),
                    '__VIEWSTATEGENERATOR': re.search(r'id="__VIEWSTATEGENERATOR" value="([^"]+)"', response_category.content,
                                                      re.I | re.S).group(1),
                    '__EVENTVALIDATION': re.search(r'id="__EVENTVALIDATION" value="([^"]+)"', response_category.content,
                                                   re.I | re.S).group(1),
                    't_web_lookup__profession_name': category,
                    't_web_lookup__first_name': '',
                    't_web_lookup__license_type_name': '',
                    't_web_lookup__last_name': '',
                    't_web_lookup__license_no': '',
                    'sch_button':'Search',
                }

                response_category_search = self.s.post(
                    url='http://verify.sos.ga.gov/Verification/Search.aspx',
                    data=data,
                    allow_redirects=True,
                )
                if response_category_search.status_code == 200:

                    has_nextpage = True
                    while has_nextpage:
                        self.getLinks(response_category_search.content)
                        responseNextpage = self.getNextpage(response_category_search)
                        if responseNextpage:
                            response_category_search = responseNextpage
                        else:
                            print 'Done.'
                            break


if __name__ == '__main__':

    q = Queue()
    lock = threading.Lock()

    script = ProfLicGeorgia(1,q,lock)
    script.setDaemon(True)
    list = script.getCategories()


    if len(list) > 0:

        for category in list:
            q.put(category)
        print 'Loaded categories'

        number_of_threads = 30
        list_of_thread = []
        for num in range(number_of_threads):
            script = ProfLicGeorgia(num,q,lock)
            script.setDaemon(True)
            script.start()
            list_of_thread.append(script)

        for i in list_of_thread:
            i.join()

        q.join()
        print 'Done.'