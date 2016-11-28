import cPickle
import gzip
import redis
from metrominy.cleaner import tokenizing
from metrominy.cosine import cosine_similarity
from metrominy.tfidf import idf
from metrominy.tfidf import qtf
from metrominy.tfidf import tf
from metrominy.tfidf import weighting_docs
from metrominy.tfidf import weighting_query





class ClassBasedPyTerm(object):

    def __init__(self, *args, **kwargs):
        self._data_tf = {}
        self._data_idf = {}
        self._data_query = {}
        self._data_qtf = {}
        self._data_weighting_docs = {}
        self._data_weighting_query = {}
        self._data_cosine = {}

        if 'data_tf' in kwargs:
            self._data_tf = kwargs['data_tf']

        if 'data_idf' in kwargs:
            self._data_idf = kwargs['data_idf']

        if 'data_query' in kwargs:
            self._data_query = kwargs['data_query']

        if 'data_qtf' in kwargs:
            self._data_qtf = kwargs['data_qtf']

        if 'data_weighting_docs' in kwargs:
            self._data_weighting_docs = kwargs['data_weighting_docs']

        if 'data_weighting_query' in kwargs:
            self._data_weighting_query = kwargs['data_weighting_query']

    def get_tf(self):
        return self._data_tf


class DocManager(ClassBasedPyTerm):

    def __init__(self, *args, **kwargs):
        self._docs = {}
        if 'data_docs' in kwargs:
            self._docs = kwargs['data_docs']
            self.__clean_doc()
        super(DocManager, self).__init__(*args, **kwargs)

    def add_docs(self, key, doc):
        self._docs[key] = tokenizing(doc)

    def __clean_doc(self):
        if self._docs:
            for k, v in self._docs.items()[:]:
                self._docs[k] = tokenizing(v)


class Indexer(DocManager, ClassBasedPyTerm):

    INDEX = 'INDEX'
    TF = 'TF'
    IDF = 'IDF'

    def __init__(self, *args, **kwargs):
        super(Indexer, self).__init__(*args, **kwargs)

    def build(self):
        # Build term frequency
        self._data_tf = tf(self._docs)
        self._data_idf = idf(self._docs, self._data_tf)
        return {
            self.TF: self._data_tf,
            self.IDF: self._data_idf
        }

    def load(self, **kwargs):
        if kwargs:
            r = redis.StrictRedis(host=kwargs['host'], port=kwargs['port'], db=kwargs['db'])
        else:
            r = redis.StrictRedis(host='localhost', port=6379, db=0)

        data = cPickle.loads(r.get(self.INDEX))
        self._data_tf = data[self.TF]
        self._data_idf = data[self.IDF]
        return data

    def save(self, **kwargs):
        try:
            if kwargs:
                r = redis.StrictRedis(host=kwargs['host'], port=kwargs['port'], db=kwargs['db'])
            else:
                r = redis.StrictRedis(host='localhost', port=6379, db=0)

            data = cPickle.dumps(self.build())
            r.set(self.INDEX, data)
            return True
        except:
            return False


class Query(Indexer):

    def __init__(self, *args, **kwargs):
        # Todo: check data di redis ! berikan exception jika datanya belum dibuild (indexer).
        super(Query, self).__init__(*args, **kwargs)

    def search(self):
        self.load()
        # Build qtf
        self._data_qtf = qtf(self._data_query)
        # Build weighting
        self._data_weighting_docs = weighting_docs(self._data_tf, self._data_idf, self._data_qtf)
        self._data_weighting_query = weighting_query(self._data_qtf, self._data_idf)

        # Cosine
        self._data_cosine = cosine_similarity(self._data_weighting_docs, self._data_weighting_query)

        return self._data_cosine


def test1():
    # Build tfidf data (build indexer)
    index = Indexer()
    index.add_docs('doc1', 'the game of life is a game of everlasting learning')
    index.add_docs('doc2', 'the unexamined life is not worth living')
    index.add_docs('doc3', 'never stop learning')
    # print index.build()
    index.save()


def test2():
    # Load tfidf data (load indexer)
    index = Indexer()
    from pprint import pprint as pp
    pp(index.load())

def test3():
    # Search processing
    query = Query(data_query='life learning')
    print query.search()
