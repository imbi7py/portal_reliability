from krwordrank.word import KRWordRank
import os,sys

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# path = os.path.join(BASE_DIR, 'analyze/lalaland_ㅅ.txt')
#
# with open(path, 'rt', encoding='UTF8') as data:
#     docs = data.readlines()
#     print(docs)

# min_count = 5   # 단어의 최소 출현 빈도수 (그래프 생성 시)
# max_length = 10 # 단어의 최대 길이
# wordrank_extractor = KRWordRank(min_count, max_length)
#
#
# beta = 0.85    # PageRank의 decaying factor beta
# max_iter = 10
# verbose = True
# # texts = ['예시 문장 입니다', '여러 문장의 list of str 입니다', ... ]
# keywords, rank, graph = wordrank_extractor.extract(docs, beta, max_iter, verbose)
#
# for word, r in sorted(keywords.items(), key=lambda x:x[1], reverse=True)[:30]:
#         print('%8s:\t%.4f' % (word, r))
from krwordrank.word import summarize_with_keywords
from krwordrank.sentence import summarize_with_sentences  # 키워드를 많이 포함한 문장을 핵심 문장으로 선택
from web_crawl.function import make_morpheme
# texts = []
def summary(list):
    keyword_list = []
    penalty = lambda x:0 if (25 <= len(x) <= 80) else 1 #문장 길이
    stopwords = {'이러한', '일단', '제가', '이거', '아니라', '때문에'}

    keywords, sents = summarize_with_sentences(
        list,
        penalty=penalty,
        stopwords = stopwords,
        diversity=0.05,
        num_keywords=100,
        num_keysents=10,
        verbose=False,
        beta = 0.85,
        max_iter = 100
    )
    print(keywords)
    wordrank_extractor = KRWordRank(
        min_count=5,  # 단어의 최소 출현 빈도수 (그래프 생성 시)
        max_length=10,  # 단어의 최대 길이
        verbose=True
    )

    beta = 0.85  # PageRank의 decaying factor beta
    max_iter = 30

    keywords, rank, graph = wordrank_extractor.extract(list, beta, max_iter)
    print(keywords)
    # keyword_list.append(keywords)
    # sents = ".".join(sents)
    # return sents
    # print(sents)
    # make_sentence(sents)
# from krwordrank.word import summarize_with_keywords
#
# keywords = summarize_with_keywords(texts, min_count=5, max_length=10,
#     beta=0.85, max_iter=10, stopwords=stopwords, verbose=True)
# keywords = summarize_with_keywords(texts) # with default arguments