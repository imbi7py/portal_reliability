import textrank
# from textrank import v
import os,sys
from web_crawl.function import summary
from textrank import KeywordSummarizer, KeysentenceSummarizer

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(BASE_DIR, 'analyze/lalaland.txt')

with open(path, 'rt', encoding='UTF8') as data:
    docs = data.readlines()
    print(docs)

'''
keyword_extractor = KeywordSummarizer(
    tokenize = lambda x:x.split(" "),      # YOUR TOKENIZER
    window = -1,
    verbose = False
)

keywords = keyword_extractor.summarize(docs, topk=50)
print(keywords)
# for word, rank in keywords:
#     print(word, rank)
#
# print(keywords)
# TextRank
# https://lovit.github.io/nlp/2019/04/30/textrank/
#
# from konlpy.tag import Kkma
#
# kkma = Kkma()
# def kkma_tokenize(sent):
#     words = kkma.pos(sent, join=True)
#     # words = [w for w in words if ('/NN' in w or '/XR' in w or '/VA' in w or '/VV' in w)]
#     words = [w for w in words if ('/NN' in w or '/XR' in w or '/VA' in w or '/VV' in w)]
#     return words
#
summarizer = KeysentenceSummarizer(
    tokenize = lambda x:x.split(" "),
    window = -1,
    verbose = False
)
#
keywords = keyword_extractor.summarize(docs, topk=30)
# print(keywords)
# summarizer = KeysentenceSummarizer(tokenize = kkma_tokenize, min_sim = 0.3)
keysents = summarizer.summarize(docs, topk=3)
print(keysents)
# make_sentence(keysents)
'''
print(summary(docs))
