# -*- coding: utf-8 -*-
#
"""preprocessing article/abstract pair
"""

# neologdnによる正規化を実施
# ref: http://yukinoi.hatenablog.com/entry/2015/10/11/205006
import neologdn
import re

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

def main():
    #x = "こんこん、ふぉっくす紺子だよ！お花見日和なのに、おしごと【紺子にゅうす】"
    x = "新型iPad情報でビンゴも！ITのいまを伝える【デジ通】まとめ読み"
    #print(remove_brackets(x))
    print(x)
    # print(call_neologdn(x))
    print(to_lowercase(x))

if __name__ == '__main__':
    main()
