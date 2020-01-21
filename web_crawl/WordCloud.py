import nltk
from konlpy.corpus import kolaw
from konlpy.tag import Kkma
from konlpy.tag import Twitter; t=Twitter()
import matplotlib.pyplot as plt
import platform
from wordcloud import WordCloud
import numpy as np
from PIL import Image
from wordcloud import ImageColorGenerator
# t=Kkma()


ko_con_text = kolaw.open('constitution.txt').read()
# ko_con_text
tokens_ko = t.nouns(ko_con_text)
# tokens_ko
# print(tokens_ko)

# print(tokens_ko)
ko = nltk.Text(tokens_ko, name='연습')
# print(ko)
data = ko.vocab().most_common(100)
print(data)


from matplotlib import font_manager, rc
if platform.system() == 'Darwin':
    rc('font', family='AppleGothic.ttf')
elif platform.system() == 'Windows':
    font_name= font_manager.FontProperties(fname="c:/Windows/fonts/malgun.ttf").get_name()
    rc('font', family=font_name)
else:
    print('unknown...')


# data = ko_con_text.vocab().most_common(500)
# data=ko
tmp_data = dict(data)


# plt.figure(figsize=(16,8))
# plt.imshow(wordcloud)
# plt.axis("off")
# plt.show()

korea_coloring = np.array(Image.open("bb.jpg"))
image_colors = ImageColorGenerator(korea_coloring)
wordcloud= WordCloud(font_path = 'c:\\windows\\fonts\\NanumGothic.ttf',
                     relative_scaling=0.1,
                     mask=korea_coloring,
                     background_color='white',
                     min_font_size=4,
                     max_font_size=40,
                     ).generate_from_frequencies(tmp_data)
plt.figure(figsize=(12,12))
plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")
plt.show()

