# -*- coding: utf-8 -*-
#
"""preprocessing article/abstract pair
"""

# neologdnによる正規化を実施
# ref: http://yukinoi.hatenablog.com/entry/2015/10/11/205006
import neologdn
import re
import argparse

brackets_pair = re.compile('【.*】$')

def remove_brackets(input):
    """末尾の隅付き括弧で囲まれた部分を除去
    """
    output = re.sub(brackets_pair, '', input)
    return output

def call_neologdn(input):
    output = neologdn.normalize(input)
    return output

def to_lowercase(input):
    output = input.lower()
    return output

def normalize_file(in_fname, out_fname):
    with open(in_fname, 'r') as rf, open(out_fname, 'w') as wf:
        for line in rf:
            n = call_neologdn(line)
            n = remove_brackets(n)
            n = to_lowercase(n)
            wf.write(n)

def get_args():
    p = argparse.ArgumentParser()
    p.add_argument('--input-article', default='article.txt')
    p.add_argument('--input-abstract', default='abstract.txt')
    p.add_argument('--output-article', default='pp-article.txt')
    p.add_argument('--output-abstract', default='pp-abstract.txt')
    args = p.parse_args()
    return args

def main():
    args = get_args()
    normalize_file(args.input_article, args.output_article)
    normalize_file(args.input_abstract, args.output_abstract)

if __name__ == '__main__':
    main()
