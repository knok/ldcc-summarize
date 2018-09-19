# -*- coding: utf-8 -*-
#
FNAME=ldcc-20140209.tar.gz

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

all: pp-abstract.txt pp-article.txt

#
clean:
	-rm -rf text
	rm -f abstract.txt article.txt
	rm -f pp-abstract.txt pp-article.txt
