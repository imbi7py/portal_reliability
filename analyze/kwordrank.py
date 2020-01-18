from krwordrank.sentence import summarize_with_sentences  # 키워드를 많이 포함한 문장을 핵심 문장으로 선택

def summary(list):
    penalty = lambda x:0 if (25 <= len(x) <= 80) else 1 #문장 길이
    stopwords = {'이러한', '일단', '제가', '이거', '아니라', '때문에'}

    keywords, sents = summarize_with_sentences(
        list,
        penalty=penalty,
        stopwords=stopwords,
        diversity=0.7,
        num_keywords=100,
        num_keysents=10,
        scaling=lambda x: 1,
        verbose=False,
    )
    return sents