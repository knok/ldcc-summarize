<!-- -*- coding: utf-8 -*- -->
# Preprocessing Livedoor News corpus for summarize

このツールは、[ライブドアニュースコーパス](https://www.rondhuit.com/download.html)を取得してseq2seq等に利用できる要約のためのデータに変換するものです。

## 必要なもの

* Python 3.6+
  * [neologdn](https://github.com/ikegami-yukino/neologdn) 日本語正規化ライブラリ
* wget
* MeCab

## 使い方

make allを実行するとコーパスをダウンロードし、展開して正規化、分かち書きをして最終的に以下の2つのファイルを生成します。

* 訓練用見出し、本文
  * train-abstract.txt
  * train-article.txt
* 評価用見出し、本文
  * test-abstract.txt
  * test-article.txt

### 分かち書き時に辞書を指定したい場合

make MECAB_OPTS="-b 40000 -d /path/to/dict"などとしてください。

## data source

もととなるデータは[CreativeCommons 2.1 BY-ND](https://creativecommons.org/licenses/by-nd/2.1/jp/)のもと配布されています。このツールで処理した結果の直接の再配布はライセンス上認められない点に注意してください。

* https://www.rondhuit.com/download.html
* https://www.rondhuit.com/download/ldcc-20140209.tar.gz

## 本スクリプトのライセンス

The MIT License (MIT) Copyright (c) 2018 NOKUBI Takatsugu

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

