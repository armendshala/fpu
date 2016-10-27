
# Numbers
# Character
# Category
# Other

from multiprocessing import Pool
import requests

def ruaj(id_):
    with open('Id.txt','ab') as a:
        a.write(str(id_) + '\n')

def download(numri):
    url = "http://www.sos.arkansas.gov/corps/search_corps.php"

    querystring = {"DETAIL": numri}

    headers = {
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        'accept-encoding': "gzip, deflate, sdch",
        'accept-language': "en-US,en;q=0.8",
        'cookie': "__utmt=1; __utma=105621121.130817150.1476360929.1476360929.1477559000.2; __utmb=105621121.5.10.1477559000; __utmc=105621121; __utmz=105621121.1477559000.2.2.utmcsr=tm.firmagraphix-ks.com|utmccn=(referral)|utmcmd=referral|utmcct=/index.php",
        'cache-control': "no-cache",
        'postman-token': "e0ff2236-e97b-f456-79df-15361b275c92"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    print 'Downlaoded: %s' % numri
    ruaj(numri)

if __name__ == '__main__':

    inserted = [str(x).strip() for x in open('Id.txt','rb')]
    total = [str(x) for x in range(1, 10)]

    notInserted = []
    for i in total:
        if i not in inserted:
            notInserted.append(i)

    notIn = set(total) - set(inserted)

    print 'Inserted:', inserted
    print 'Total:', total
    print 'Not Inserted:', notInserted
    print 'Not Inserted _:', list(notIn)

    p = Pool(1)
    p.map(download,notInserted)