from textrank import KeywordSummarizer
import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(BASE_DIR, 'analyze/lalaland.txt')

with open(path, 'rt', encoding='UTF8') as data:
   docs = data.readlines()

keyword_extractor = KeywordSummarizer(
    tokenize = lambda x:x.split(),      # YOUR TOKENIZER
    window = -1,
    verbose = False
)

keywords = keyword_extractor.summarize(docs, topk=30)
# print(keywords)
# for word, rank in keywords:
    # do something


# TextRank
# https://lovit.github.io/nlp/2019/04/30/textrank/

from konlpy.tag import Komoran

komoran = Komoran()
def komoran_tokenize(sent):
    words = komoran.pos(sent, join=True)
    words = [w for w in words if ('/NN' in w or '/XR' in w or '/VA' in w or '/VV' in w)]
    return words

from textrank import KeywordSummarizer

keyword_extractor = KeywordSummarizer(
    tokenize = komoran_tokenize,
    window = -1,
    verbose = False
)

# keywords = keyword_extractor.summarize(docs, topk=30)

from textrank import KeysentenceSummarizer

summarizer = KeysentenceSummarizer(tokenize = komoran_tokenize, min_sim = 0.3)
keysents = summarizer.summarize(docs, topk=3)
print(keysents)