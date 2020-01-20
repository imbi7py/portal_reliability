import os
from urllib.parse import urlparse

import requests
from konlpy.tag import Kkma

from web_crawl.BlogCrawling import Naver
from web_crawl.function import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(BASE_DIR, 'web_crawl/sub_word.txt')

with open(path, 'rt', encoding='ANSI') as data:
    words = data.readlines()
    words = list(map(lambda s: s.rstrip(), words))


page_info_list = []
def get_api_result(keyword, display, start):
    url = "https://openapi.naver.com/v1/search/blog?query=" + keyword +"&display=" +str(display)\
          +"&start=" +str(start)+ "&sort=sim"     # 유사성을 기준으로
    result = requests.get(urlparse(url).geturl(),
                          headers={"X-Naver-Client-Id": "GQKArseCDOh1t1AMHtxQ",
                                   "X-Naver-Client-Secret": "yf6tWSa_Zl"})
    return result.json()

def call_and_print(keyword, page):
    json_obj = get_api_result(keyword, 30, page)
    for item in json_obj['items']:
        title = item['title'].replace("<b>", "").replace("</b>", "").replace("&lt;", "").replace("&gt;", "").replace("&quot;","")
        link = item['link']
        result = (title, link)
        page_info_list.append(result)

Naver_list = []
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

count=1
for i in range(len(page_info_list)):
    Naver_list.append(Naver(page_info_list[i][1]))
    # title_list.append(link[0])
    imoti_count_list.append(Naver_list[i][0])
    img_count_list.append(Naver_list[i][1])
    video_count_list.append(Naver_list[i][2])
    content_str_list.append(Naver_list[i][3])

# print(content_str_list)
kkma = Kkma()
for i in range(len(content_str_list)):
    content_str_list[i] = kkma.sentences(content_str_list[i])
    # content_str_list[i] = re.split(r"-|\*|\.", content_str_list[i])
    # for content in content_str_list[i]:
    #     content = content.strip().strip()
    #     content = content.replace(" ","")
    content_str_list[i] = list(filter(None, content_str_list[i]))
    content_str_list[i] = list(filter(lambda x:x not in words, content_str_list[i]))
    print(count,content_str_list[i])
    print(count,summary(content_str_list[i]))
    count +=1

# for i in range(len(page_info_list)):
#     print(count, page_info_list[i][1])
#     print(count,imoti_count_list[i])
#     print(count,img_count_list[i])
#     print(count,video_count_list[i])
#     print(count, content_str_list[i])
#     print(count, summary_content[i])
#     print()
#     print("===============================================================================================================")
#     print()
#     count += 1
# for i in range(len(summary_content)):
#     morpheme_list.append(make_morpheme(summary_content[i]))
# print(morpheme_list)
#
# for i in range(len(morpheme_list)):
#     select_morphs_list.append(select_morpheme(morpheme_list[i]))
#     print(select_morphs_list[i])