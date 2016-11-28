from unittest import TestCase
from metrominy import Indexer


class TestBuild(TestCase):

    def test_build_data(self):
        data_sample = {
            'IDF': {
                 'a': 2.09861228866811,
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

            'TF': {
                 'doc1': {
                     'a': 0.1,
                     'everlasting': 0.1,
                     'game': 0.2,
                     'is': 0.1,
                     'learning': 0.1,
                     'life': 0.1,
                     'of': 0.2,
                     'the': 0.1},
                 'doc2': {
                     'is': 0.14285714285714285,
                     'life': 0.14285714285714285,
                     'living': 0.14285714285714285,
                     'not': 0.14285714285714285,
                     'the': 0.14285714285714285,
                     'unexamined': 0.14285714285714285,
                     'worth': 0.14285714285714285},
                 'doc3': {
                     'learning': 0.3333333333333333,
                     'never': 0.3333333333333333,
                     'stop': 0.3333333333333333},}}

        index = Indexer()
        index.add_docs('doc1', 'the game of life is a game of everlasting learning')
        index.add_docs('doc2', 'the unexamined life is not worth living')
        index.add_docs('doc3', 'never stop learning')

        self.assertDictEqual(data_sample, index.build())

