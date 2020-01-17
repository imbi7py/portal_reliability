# from konlpy.tag import Twitter
from konlpy.tag import Kkma
from collections import Counter

def make_morpheme(list):
    kkma = Kkma()
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
 