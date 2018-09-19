# -*- coding: utf-8 -*-
#
"""データを訓練用、テスト用に分割、内容の入れ替えも実施
"""

import argparse
import numpy as np

def get_lines(fname):
    count = 0
    with open(fname, 'r') as f:
        for line in f:
            count += 1
    return count

def get_args():
    p = argparse.ArgumentParser()
    p.add_argument('--input-abstract', default='wakati-pp-abstract.txt')
    p.add_argument('--input-article', default='wakati-pp-article.txt')
    p.add_argument('--output-train-abstract', default='train-abstract.txt')
    p.add_argument('--output-train-article', default='train-article.txt')
    p.add_argument('--output-test-abstract', default='test-abstract.txt')
    p.add_argument('--output-test-article', default='test-article.txt')
    p.add_argument('--train-ratio', type=float, default=0.9)
    args = p.parse_args()
    return args

def main():
    args = get_args()
    counts = get_lines(args.input_abstract)
    index = np.arange(counts)
    np.random.shuffle(index)
    train_idx, test_idx = np.split(index, [int(counts * args.train_ratio)])

    #
    with open(args.input_abstract, 'r', errors='ignore') as bf, open(args.input_article, 'r', errors='ignore') as rf, \
         open(args.output_train_abstract, 'w') as tbf, open(args.output_train_article, 'w') as trf, \
         open(args.output_test_abstract, 'w') as ebf, open(args.output_test_article, 'w') as erf:
        count = 0
        for abst, art in zip(bf, rf):
            if count in train_idx: # for train data
                tbf.write(abst)
                trf.write(art)
            else:
                ebf.write(abst)
                erf.write(art)
            count += 1

if __name__ == '__main__':
    main()










