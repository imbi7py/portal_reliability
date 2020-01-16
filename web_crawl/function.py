from konlpy.tag import Twitter
from collections import Counter

def make_sentence(list):
    twitter = Twitter()
    sentences_tag = []
    #형태소 분석하여 리스트에 넣기
    for sentence in list:
        morphs = twitter.pos(sentence[3]) # pos메소드 : 형태소 분석해줌
        # sentences_tag.append(morph)
        # print(morphs)
        # print('-' * 30)
 
    # print(sentences_tag)
    # print('\n' * 3)
    # print(morphs)
    sentence_list = []
    for morph in morphs:
        if morph[1] in ['Noun', 'Adjective', 'Verb']:
            sentence_list.append(morph)
    print(sentence_list)
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
    counts = Counter(sentence_list)
    print(counts)
    # tags = counts.most_common(list)
    # print(counts)
    # print(tags)
 