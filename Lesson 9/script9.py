
# Numbers
# Character
# Category
# Other

from multiprocessing import Pool

import notin
import re
import requests
import string

def ruaj(id_):
    with open('Id.txt','ab') as a:
        a.write(str(id_) + '\n')

def download(character):

    url = "http://www.sos.arkansas.gov/corps/search_corps.php"

    payload = "SEARCH=Search&agent_city=&agent_search=&agent_state=&cmd=&corp_name={0}&corp_type_id=&fict_name=&filing_number=".format(character)
    headers = {
        'origin': "http://www.sos.arkansas.gov",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        'content-type': "application/x-www-form-urlencoded",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        'referer': "http://www.sos.arkansas.gov/corps/search_corps.php?corp_name={0}&".format(character),
        'accept-encoding': "gzip, deflate",
        'accept-language': "en-US,en;q=0.8",
        'cache-control': "no-cache",
        'postman-token': "0e3f6035-c185-682e-c5e9-5041ad50e178"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    list_ids = re.findall(r'(?si)<a href="search_corps\.php\?DETAIL=(\d+)&', response.content,re.I|re.S)
    for id_ in list_ids:
        print id_

    print 'Character: %s' % character
    ruaj(character)

# def notInserted():
#     characters = []
#     for i in string.ascii_lowercase:
#         for j in string.ascii_lowercase:
#             characters.append(i + j)
#
#     inserted = [str(x).strip() for x in open('Id.txt', 'rb')]
#     notIn = set(characters) - set(inserted)
#     return list(notIn)

if __name__ == '__main__':



    notInserted_ = notin.notInserted()
    p = Pool(10)
    p.map(download,notInserted_)