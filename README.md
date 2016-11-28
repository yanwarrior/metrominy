# metrominy


Metrominy is a simple package that implements the method term frequency and inverse document frequency for weighting collection of documents by providing value to the cosine similarity search results of a search query.

This package purely weighting and calculation of similarity and does not yet include preprocessing. You can look for some package to support the preprocessing appropriate document language that you use for preprocessing which consists of tokenizing, filtering and stemming. for stemming Indonesian words can refer [This](https://pypi.python.org/pypi/Sastrawi/1.0.1) package.

## Basic knowledge

If you are really new about text mining and basic weighting. This package uses methods Tf-Idf and Cosine Similarity. This topic relates about text mining. You can read about [Text Mining](https://en.wikipedia.org/wiki/Text_mining) and
[Tf-Idf](https://en.wikipedia.org/wiki/Tf%E2%80%93idf).

## Required

This package works on `Python 2.7` and `Python 3` does not support.

## Installation

This package is available at PyPI. You can install it via pip command line:

```
$ pip install metrominy
```

for manual installation, please clone this repository and install with setup.py:

```
$ python setup.py install
```

## Dependencies

This package has a dependency on the package [python-redis](http://github.com/andymccurdy/redis-py). however, the setup will automatically install any required packages. For Redis, you can visit the [official website redis](https://redis.io/).

### Quick Start (Build)

There are several steps in the search process in this package. Your first step should generate Term Frequency and Inverse Document Frequency of the documents that you add as a collection:

```python
>>> from metrominy import Indexer
>>>
>>> index = Indexer()
>>> # Add documents
>>> index.add_docs('doc1', 'the game of life is a game of everlasting learning')
>>> index.add_docs('doc2', 'the unexamined life is not worth living')
>>> index.add_docs('doc3', 'never stop learning')
>>>
>>> # Build Tf-Idf from all documents given
>>> index.save()
```

This data will be stored into Redis as binary data. You can check by using Redis cli with keywords `INDEX`:

```
127.0.0.1:6379> GET INDEX
"(dp1\nS'tf'\np2\n(dp3\nS'doc2'\np4\n(dp5\
nS'unexamined'\np6\nF0.14285714285714285\nsS'living'
....."
```

### Load Indexer
The next step is the process of loading data. This step takes all the data from the binary index Redis be built-in index data. This process will be used when searching:

```python
>>> from metrominy import Indexer
>>>
>>> index = Indexer()
>>> index.load()
 'TF': {'doc1': {'a': 0.1,
             'everlasting': 0.1,
             'game': 0.2,
             'is': 0.1,
             'learning': 0.1,
             'life': 0.1,
             'of': 0.2,
             'the': 0.1},
    'doc2': {'is': 0.14285714285714285,
             'life': 0.14285714285714285,
             'living': 0.14285714285714285,
             'not': 0.14285714285714285,
             'the': 0.14285714285714285,
             'unexamined': 0.14285714285714285,
             'worth': 0.14285714285714285},
    'doc3': {'learning': 0.3333333333333333,
             'never': 0.3333333333333333,
             'stop': 0.3333333333333333}}}
    {'IDF': {'a': 2.09861228866811,
             'everlasting': 2.09861228866811,
             'game': 2.09861228866811,
             'is': 1.4054651081081644,
             'learning': 1.4054651081081644,
             'life': 1.4054651081081644,
             'living': 2.09861228866811,
             'never': 2.09861228866811,
             'not': 2.09861228866811,
             'of': 2.09861228866811,
             'stop': 2.09861228866811,
             'the': 1.4054651081081644,
             'unexamined': 2.09861228866811,
             'worth': 2.09861228866811},
```

### Searching
This step is important. involves the query data that will be used as the cosine value calculation. the result is the cosine similarity values for each document you want to search from a given query. tolerance limit value of similarity is 0.9 and 1.0:

```python
>>> from metrominy import Query
>>>
>>> query = Query(data_query='life learning')
>>> query.search()
{'doc2': 0.7071067811865476,
 'doc3': 0.7071067811865475,
 'doc1': 1.0}
```

### Test
to test, we need a package nose. Type the following command to install package nose:

```
$ pip install nose
$ nosetests
```

Then, to run tests, we can simply do::

```
python setup.py test
```

Test can be okay if result:

```
----------------------------------------------------------------------
Ran 1 test in 0.060s

OK
```
## License

> The MIT License (MIT)
Copyright © 2016 Yanwar Solahudin, <yanwarsolah@gmail.com>

> Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

> The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
