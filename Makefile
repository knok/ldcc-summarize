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

# normalize

# word segmentation
