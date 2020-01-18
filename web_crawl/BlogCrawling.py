import bs4
from selenium import webdriver
from datetime import datetime
import lxml


options = webdriver.ChromeOptions()
options.add_argument('headless') # 팝업창 안띄우는 속성

options.add_argument("disable-gpu")
driver = webdriver.Chrome('chromedriver', chrome_options=options)


def Naver(url):
    driver.get(url)  # se-main-container 속성 블로그
    driver.implicitly_wait(3)
    driver.switch_to.frame('mainFrame')
    html = driver.page_source

    bs_obj = bs4.BeautifulSoup(html, "lxml")
    ul = bs_obj.find("div", {"class":"se-main-container"})
    ul1 = bs_obj.find("div", {"class": "se_component_wrap sect_dsc __se_component_area"})

    if ul:
        ul = bs_obj.find("div", {"class": "se-main-container"})  # 본문 영역 가져오기

        # lis= str(ul.findAll("p"))
        lis = ul.findAll("p")  # 문장이 있는 p 태그 추출
        lis2 = ul.findAll("img", {"class": "se-sticker-image"})  # 이모티콘 추출
        image = ul.findAll("img", {"class": "se-image-resource"})  # 이미지 추출
        canvas = ul.findAll("div", {"class": "se-component se-video se-l-default"})  # 동영상 추출

        content_list = []  # 문자를 넣어주기 위한 리스트

        for li in lis:  # \u200b 제거후 텍스트 추출
            if li.text != '\u200b':
                content_list.append(li.text.replace("\xa0", "").replace("\u200b","").strip())  # 빈 리스트에 li의 텍스트를 반복문으로 이어 붙이기

        content_str = "*".join(content_list)
        imoti_count = str(lis2).count("img")
        img_count = str(image).count("img")
        video_count = str(canvas).count("se-component se-video se-l-default")
        # print(imoti_count)
        # print(img_count)
        # print(video_count)
        # print(content_str)
        # print(type(content_str))
        result = imoti_count, img_count, video_count, content_str
        return result

    elif ul1:
        ul = bs_obj.find("div", {"class":"se_component_wrap sect_dsc __se_component_area"}) # 본문 영역 가져오기
        image = ul.findAll("div", {"class": "se_component se_image default"}) #이미지 추출
        lis2 = ul.findAll("img", {"class": "__se_img_el"}) #이모티콘 추출
        canvas = ul.findAll("div", {"class": "_video_thumb"}) # 동영상 추출

        lis= ul.findAll("p")
        content_list = [] #문자를 넣어주기 위한 리스트

        for li in lis:  # \u200b 제거후 텍스트 추출
            content_list.append(str(li.text.replace("\xa0", "").replace("\u200b","").strip())) #빈 리스트에 li의 텍스트를 반복문으로 이어 붙이기

        content_str = "*".join(content_list)
        imoti_count = str(lis2).count("스티커 이미지")
        img_count = str(image).count("imgId")
        video_count = str(canvas).count("_video_thumb")
        # print(imoti_count)
        # print(img_count)
        # print(video_count)
        # print(content_str)
        # print(type(content_str))
        result = imoti_count, img_count, video_count, content_str
        return result

    else:
        ul = bs_obj.find("div", {"id": "postViewArea"})

        content_list = []
        # content1 = ul.findAll("div")
        # content2 = ul.findAll("p")
        #
        # if content1 == None:
        #     for content in content2:
        #         content_list.append(content.text)
        # else:
        #     for content in content1:
        #         content_list.append(content.text)
        contents = ul.findAll("p")
        for content in contents:
            content_list.append(content.text.replace("\xa0", "").replace("\u200b","").strip())


        lis2 = ul.findAll("img")

        image = ul.findAll("img", {"class": "_photoImage"})

        canvas = ul.findAll("div", {"class": "_video_thumb"})  # 동영상 추출

        content_str = "*".join(content_list)
        imoti_count = str(lis2).count("type=p50_50")
        img_count = str(image).count("img")
        video_count = str(canvas).count("_video_thumb")
        # print(imoti_count)
        # print(img_count)
        # print(video_count)
        # # print(content_list)
        # print(content_str)
        # print(type(content_str))
        result = imoti_count, img_count, video_count, content_str
        return result
