#!/usr/bin/env python
# coding=utf-8

from __future__ import print_function
from glob import glob
from sklearn.feature_extraction.text import CountVectorizer

from mr import Job, Reader, Runner
from count_words import FileReader


class Transformer(Job):
    def __init__(self, reader, transform_func):
        super(Transformer, self).__init__(reader)
        self.transform_func = transform_func

    def map(self):
        self.result = [self.transform_func(self.reader.read())]

    def reduce(self, other):
        self.result.extend(other.result)

    @classmethod
    def create_jobs(cls, reader_class, config):
        jobs = []
        for reader in reader_class.create_readers(config):
            jobs.append(cls(reader, config['transform_func']))
        return jobs


def create_vectorizer():
    count_vectorizer = CountVectorizer(analyzer='char')
    reader = FileReader('./pred.txt')
    count_vectorizer.fit(reader.read())
    return count_vectorizer


if __name__ == '__main__':
    count_vectorizer = create_vectorizer()
    config = {}
    config['files'] = glob('./*.txt')
    config['transform_func'] = count_vectorizer.transform
    runner = Runner(Transformer, FileReader, config)
    transformed_matrixes = runner.run()
    for X in transformed_matrixes:
        print(u'Трансформированная матрица:\nТип:{}, размерность: {}, сумма элементов: {}'.format(type(X), X.shape, X.sum()))
