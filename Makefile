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

# word segmentation

all: abstract.txt article.txt

#
clean:
	-rm -rf text
	rm -f abstract.txt article.txt
