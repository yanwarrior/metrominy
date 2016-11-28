from __future__ import division
from collections import Counter
from math import log


def tf(docs={}):
    total = 0
    result = {}

    # Mencari nilai term frequency pada setiap dokumen
    for key, doc in docs.items():
        result[key] = dict(Counter(doc.split(' ')))

    # Mencari nilai normalized term frequency
    for key, terms in result.items():
        # total adalah jumlah seluruh term
        total = sum(terms.values())
        for term, val in terms.items():
            result[key][term] = val / total

    return result


def idf(docs={}, tf={}):
    # total adalah jumlah keseluruhan dokumen
    total = len(docs.keys())
    result = {}

    # mengambil semua term secara distinct
    term_dist = [doc for doc in docs.values()]
    term_dist = ' '.join(term_dist)
    term_dist = set(term_dist.split(' '))

    # menghitung IDF
    for term in term_dist:
        appears = 0
        for key, doc in docs.items():
            if term in doc.split(' '):
                # menghitung kejadian term pada setiap dokumen
                # setiap term yang ada di dalam dokumen saat ini
                # maka nilai appears ditambahkan 1
                appears += 1

        # menghitung logaritma
        log2 = 1.0 + log(total / appears)

        # jika nilai log2 kurang atau sama dengan 0
        # maka nilai log2 diubah ke 1.0
        if log2 <= 0:
            log2 = 1.0

        result[term] = log2

    return result


def weighting_docs(data_tf={}, data_idf={}, data_qtf={}):
    result = {}
    for k1, v1 in data_tf.items():
        result[k1] = {}
        for k2, v2 in data_qtf.items():
            if k2 in v1.keys() and k2 in data_idf.keys():
                result[k1][k2] = v1[k2] * data_idf[k2]
            else:
                result[k1][k2] = 0.0
    return result


def weighting_query(data_qtf={}, data_idf={}):
    result = {}
    for qterm, qvalue in data_qtf.items():
        if qterm in data_idf.keys():
            result[qterm] = qvalue * data_idf[qterm]
        else:
            result[qterm] = 0.0

    return result

def qtf(query=''):
    query = {'q': query}
    return tf(docs=query)['q']


def __proses_generate_tfidf():
    docs = {
        'doc1': 'the game of life is a game of everlasting learning',
        'doc2': 'the unexamined life is not worth living',
        'doc3': 'never stop learning',
    }

    mytf = tf(docs)
    myidf = idf(docs, mytf)


def __proses_pencarian():
    # proses load, dalam hal ini melakukan proses generate
    docs = {
        'doc1': 'the game of life is a game of everlasting learning',
        'doc2': 'the unexamined life is not worth living',
        'doc3': 'never stop learning',
    }

    data_tf = tf(docs)
    data_idf = idf(docs, data_tf)

    # proses pencarian
    query = 'life learning'

    data_qtf = qtf(query)
    data_weighting_docs = weighting_docs(data_tf, data_idf, data_qtf)
    data_weighting_query = weighting_query(data_qtf, data_idf)
    # result = cosine_similarity(data_weighting_docs, data_weighting_query)
    print data_weighting_docs
    print data_weighting_query
    # print result









