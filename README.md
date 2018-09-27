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
