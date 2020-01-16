# konlpy : 설치하기
# http://konlpy.org/ko/v0.5.2/install/#id2

from eunjeon import Mecab

# Mecab 함수를 tagger라는 이름으로 사용
tagger = Mecab() 
# 문장에서 명사만 분류
tagger.nouns("고양이가 냐 하고 울면 나는 녜 하고 울어야지")

# 빛 아래 유령
poem = """
흘러내린 머리카락이 흐린 호박빛 아래 빛난다.
유영하며.
저건가보다.
세월의 힘을 이겨낸 마지막 하나 남은 가로등.
미래의 색, 역겨운 청록색으로 창백하게 바뀔 마지막 가로등
난 유영한다. 차분하게 과거에 살면서 현재의 공기를 마신다.
가로등이 깜빡인다.
나도 깜빡여준다.
"""
# 문장을 형태소 단위로 끊어줌
tagger.morphs(poem)

# 문장을 형태소단위로 끊고, 형태소 마다 품사를 분석
# 이때, ('지우개', 'NNG')등의 형식을 분류되는데, NNG는 일반명사를 뜻
# 자세한 품사태그는 링크를 참고 : https://m.blog.naver.com/PostView.nhn?blogId=aul-_-&logNo=221557243190
print(tagger.pos(poem))
# print(tagger.nouns(poem))


