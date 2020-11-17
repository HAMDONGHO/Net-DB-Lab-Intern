import numpy as np
import re
import csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import nltk
import pandas as pd




# tfidfv = TfidfVectorizer().fit(["뿔"])

# # count_model = CountVectorizer(ngram_range=(1,1)) # default unigram model
#
# print(tfidfv.transform(['뿔']).toarray())
# tfidf_vectorizer.fit(keyword_result)
data = pd.read_csv('file_data_2020-08-01_to_2020-08-15.csv', error_bad_lines=False)

print(len(data))
sel =  data[data.date == '2020-08-01'][['text']]
sel['text'] = sel.apply(lambda row : nltk.word_tokenize(row['text']), axis=1)
# sel.apply
print(sel)
#
# with open('file_data_2020-08-01_to_2020-08-15.csv','r', -1, encoding='utf-8') as csvfile:
#     rows = csv.DictReader(csvfile, delimiter=',')
#     datas = {}
#     count = 0
#     for row in rows:
#         if row['date'] not in datas :
#             datas[row['date']] = []
#         datas[row['date']].append(row['text'])
#         count +=1
#     print(count)
#     print(datas['2020-08-01'].head(5))

    # tdm = TermDocumentMatrix(Corpus(VectorSource(datas['2020-08-01'])),
    #                       control = list(removeNumbers = T,       # 숫자 없애기
    #                                      removePunctuation = T,   # 기호 없애기
    #                                      stopwords = T,           # 스탑워즈 없애기
    #                                      wordLength = c(3, Inf)))







    # tfidfv = TfidfVectorizer().fit(datas['2020-08-01'])
    # count_model = CountVectorizer(ngram_range=(1,1)) # default unigram model
    # X = count_model.fit_transform(datas['2020-08-01'])
    # Xc = (X.T * X) # this is co-occurrence matrix in sparse csr format
    # Xc.setdiag(0) # sometimes you want to fill same word cooccurence to 0
    # # print(tfidfv.transform(datas['2020-08-01']).toarray())
    # top = 0
    # topv = ''
    # # res = sorted(tfidfv.vocabulary_.items(), key=(lambda x:x[1]))
    # # print(res)
    #
    # print(Xc.todense())
    # print(count_model.vocabulary_)

# X[X > 0] = 1 # run this line if you don't want extra within-text cooccurence (see below)
    # for v in tfidfv.vocabulary_:
    #     if tfidfv.vocabulary_[v] > top :
    #         topv = v
    #         top = tfidfv.vocabulary_[v]
