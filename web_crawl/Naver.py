import requests
from urllib.parse import urlparse
from web_crawl.BlogCrawling import Naver
from web_crawl.function import make_sentence

page_list = []

def get_api_result(keyword, display, start):
    url = "https://openapi.naver.com/v1/search/blog?query=" + keyword +"&display=" +str(display)\
          +"&start=" +str(start)    # 시작위치 설정
    result = requests.get(urlparse(url).geturl(),
                          headers={"X-Naver-Client-Id": "GQKArseCDOh1t1AMHtxQ",
                                   "X-Naver-Client-Secret": "yf6tWSa_Zl"})
    return result.json()

def call_and_print(keyword, page):
    json_obj = get_api_result(keyword, 1, page)
    for item in json_obj['items']:
        title = item['title'].replace("<b>", "").replace("</b>", "").replace("&lt;", "").replace("&gt;", "").replace("&quot;","")
        link = item['link']
        result = (title, link)
        page_list.append(result)

list = []
input = input('검색할 단어 > ')
call_and_print(input, 1)
for link in page_list:
    # print(link[0])
    list.append(Naver(link[1]))

make_sentence(list)