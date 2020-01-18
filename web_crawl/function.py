from konlpy.tag import Twitter
from konlpy.tag import Kkma
from collections import Counter




def make_morpheme(list):
    kkma = Twitter(jvmpath='C:\Program Files\Java\jdk1.8.0_231\jre\bin\server\jvm.dll')
    sentences_tag = []
    #형태소 분석하여 리스트에 넣기
    morphs = kkma.pos(list) # pos메소드 : 형태소 분석해줌
    # print(morphs)
    sentences_tag.append(morphs)
    return sentences_tag

def select_morpheme(list):
    select_list = []
    for morph in list:
        for word, tag in morph:
            if tag in ['NNG','VV', 'XR']:
               select_list.append(word)
    return select_list

from krwordrank.sentence import summarize_with_sentences  # 키워드를 많이 포함한 문장을 핵심 문장으로 선택

def summary(list):
    try:
        penalty = lambda x: 0 if (5 <= len(x) <= 80) else 1  # 문장 길이
        stopwords = {'이러한', '일단', '제가', '이거', '아니라', '때문에',
                     '동영상', '도움말', '미지원으로', '드래그', '지원되지않습니다.도움말',
                     'ㅎㅎ', '중입니다.5분', '퍼가기', 'Object', '마우스를', '인코딩', '음소',
                     '음소거', 'Flash', '영상의', '소요'}

        keywords, sents = summarize_with_sentences(
            list,
            penalty=penalty,
            stopwords=stopwords,
            diversity=0.7,
            num_keywords=100,
            num_keysents=10,
            scaling=lambda x: 1,
            beta=0.85,  # PageRank의 decaying factor beta
            max_iter=10,
            verbose=True
        )
        print(keywords)
        return sents
    except ValueError:
        print('key가 없습니다.')
        pass
    # print(sentences_tag)
    # print('\n' * 3)
    # print(morphs)
    # sentence_list = []
    # for morph in morphs:
    #     if morph[1] in ['Noun\\\', 'Adjective', 'Verb']:
    #         sentence_list.append(morph)
    # print(sentence_list)
    #         if word[1] in ['Noun', 'Adjective', 'Verb']:
    #             sentence_list.append(word)
    # print(sentence_list)
    # noun_adj_list = []
    #명사와 형용사만 구분하여 이스트에 넣기
    # for sentence1 in sentences_tag:
    #     for word, tag in sentence1:
    #         if tag in ['Noun', 'Adjective']:
    #             noun_adj_list.append(word)

    #형태소별 count
    # counts = Counter(sentence_list)
    # print(counts)
    # tags = counts.most_common(list)
    # print(counts)
    # print(tags)
 