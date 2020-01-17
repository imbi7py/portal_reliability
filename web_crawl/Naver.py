import requests
from urllib.parse import urlparse
from web_crawl.BlogCrawling import Naver
from web_crawl.function import make_morpheme, select_morpheme
from analyze.kwordrank import summary

page_list = []

def get_api_result(keyword, display, start):
    url = "https://openapi.naver.com/v1/search/blog?query=" + keyword +"&display=" +str(display)\
          +"&start=" +str(start)+ "&sort=sim"     # 유사성을 기준으로
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
title_list = []
imoti_count_list= []
img_count_list = []
video_count_list = []
content_str_list = []
summary_content = []
morpheme_list = []
select_morphs_list = []
input = input('검색할 단어 > ')
call_and_print(input, 1)
for i in range(len(page_list)):
    # print(link[0])
    list.append(Naver(page_list[i][1]))
    # print(link[1])
    # title_list.append(link[0])
    imoti_count_list.append(list[i][0])
    img_count_list.append(list[i][1])
    video_count_list.append(list[i][2])
    content_str_list.append(list[i][3])

# print(content_str_list)
count=1
for i in range(len(content_str_list)):
    summary_content.append(summary(content_str_list[i].split("*")))
    print(count,summary_content[i])
    count += 1

for i in range(len(summary_content)):
    morpheme_list.append(make_morpheme(summary_content[i]))

for i in range(len(morpheme_list)):
    select_morphs_list.append(select_morpheme(morpheme_list[i]))
    print(select_morphs_list[i])