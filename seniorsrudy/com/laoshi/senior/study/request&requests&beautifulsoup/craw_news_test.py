import requests
from bs4 import BeautifulSoup

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Host": "www.infoq.cn",
    # "Cookie": " _ga=GA1.2.1957457316.1641434836; LF_ID=1641434836521-2714673-6525485; GRID=d9d78d8-d84b04b-de13ae9-b6e1191; _gid=GA1.2.963635799.1643097200; _gat=1; Hm_lvt_094d2af1d9a57fd9249b3fa259428445=1641434836,1643097200; Hm_lpvt_094d2af1d9a57fd9249b3fa259428445=1643097200;SERVERID=1fa1f330efedec1559b3abbcb6e30f50|1643097201|1643097199",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
}
url = 'https://www.infoq.cn/news'


def craw(url):
    reponse = requests.get(url, headers=headers)
    soup = BeautifulSoup(reponse.text, 'lxml')
    print(soup)


craw(url)
