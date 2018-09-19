# -*- coding: utf-8 -*-
#
FNAME=ldcc-20140209.tar.gz
MECAB_OPTS=

# download
$(FNAME):
	wget https://www.rondhuit.com/download/$(FNAME)
# unpack
text:
	tar xvf $(FNAME)

# make article/abstract pair
abstract.txt article.txt: text
	python make_pair.py

# normalize
pp-abstract.txt pp-article.txt: abstract.txt article.txt
	python preprocess.py

# word segmentation
# TODO: take care about too longer lines
wakati-pp-abstract.txt wakati-pp-article.txt: pp-abstract.txt pp-article.txt
	mecab -Owakati $(MECAB_OPTS) < pp-abstract.txt > wakati-pp-abstract.txt
	mecab -Owakati $(MECAB_OPTS) < pp-article.txt > wakati-pp-article.txt

all: wakati-pp-abstract.txt wakati-pp-article.txt

#
clean:
	-rm -rf text
	rm -f abstract.txt article.txt
	rm -f pp-abstract.txt pp-article.txt
	rm -f wakati-pp-abstract.txt wakati-pp-article.txt
