import requests
import re
import parsel

from multiprocessing import Pool

def kryejpune(character):

    print 'Duke kerkuar shhronjen: %s' % character

    main_url = 'http://www.sosnc.gov/search/index/corp'

    with requests.Session() as session:

        session.headers.update({
            'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
        })

        response = session.get(main_url)
        if response.status_code == 200:

            data = {
                'FullSite': 'TRUE',
                'Division': 'CORPORATIONS',
                'UccSearchType': 'STANDARD',
                'LobbySearchType': 'PRINCIPAL',
                'CorpSearchType': 'CORPORATION',
                'LobbySearchTerm': 'All',
                'SearchType': 'STARTING',
                'EntityType': 'ORGANIZATION',
                'LobbySearchResign': 'RESIGNED',
                'LandSearchType': 'ANNEXATION',
                'SearchText': character,
                'IndividualsSurname': '',
                'FirstPersonalName': '',
                'AdditionalNamesInitials': '',
            }

            response_post = session.post(
                url='http://www.sosnc.gov/Search/RunSearch',
                data=data,
            )
            if response_post.status_code == 200:

                content = response_post.content

                has_nextpage = True
                while has_nextpage:

                    for link,name in re.findall(r'href="profcorp/(\d+)"><b>([^<]+)<',content,re.I|re.S):
                        link = 'http://www.sosnc.gov/Search/profcorp/%s' % link
                        print character,link,name
                        
                        response_company = session.get(link)
                        if response_company.status_code == 200:
                            content = response_company.content

                            # ruaje ne db

                    pattern_nextPage = re.search(r'<a href="([^"]+)">Next Page',content,re.I|re.S)
                    if pattern_nextPage:
                        nextPage = pattern_nextPage.group(1)
                        nextPage = 'http://www.sosnc.gov%s' % nextPage
                        nextPage = nextPage.replace('&amp;','&')

                        response_next = session.get(nextPage)
                        if response_next.status_code == 200:
                            content = response_next.content
                            print 'Next page >>'
                        else:
                            has_nextpage = False


if __name__ == '__main__':

    characteret = list()
    for i in range(65,91):
        for j in range(65,91):
            ch = '%s%s' % (chr(i),chr(j))
            characteret.append(ch)

    print len(characteret)

    p = Pool(25)
    p.map(kryejpune,characteret)

    print 'Done.'