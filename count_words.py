#!/usr/bin/env python
# coding=utf-8

from __future__ import print_function
from glob import glob
from mr import Job, Reader, Runner


class FileReader(Reader):

    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'r') as in_file:
            for line in in_file:
                yield line

    @classmethod
    def create_readers(cls, config):
        files = config['files']
        for filename in files:
            yield cls(filename)


class WordCounter(Job):
    def map(self):
        self.result = sum([len(line.split()) for line in self.reader.read()])

    def reduce(self, other):
        self.result += other.result


if __name__ == '__main__':
    # reader = FileReader('./pred.txt')
    # for line in reader.read():
    #     print(len(line.split()), line)

    config = {}
    config['files'] = glob('./*.txt')
    runner = Runner(WordCounter, FileReader, config)
    n_words = runner.run()
    print(u'Количество слов в текстовых файлах:\n{}'.format(n_words))
