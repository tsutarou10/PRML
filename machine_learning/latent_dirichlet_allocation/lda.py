# -*- coding: utf-8 -*-
#!/usr/bin/python
import logging
logging.basicConfig(format = "%(asctime)s : %(levelname)s : %(message)s",level = logging.INFO)
import numpy as np
import scipy
from gensim import corpora,models,similarities
import os
from StopWord_en import StopWords
from nltk import stem
from nltk.stem.porter import PorterStemmer
import codecs

class Lda:
	def __init__(self):
		self.lda_topics = 1000

	def set_texts(self):
		file = open("all_data.txt","r")
		documents = file.readlines()
		#sw = StopWords()
		#aa = sw.get_noise_mark_list()
		#stoplist = sw.get_swlist()
		texts = [[word for word in document.split()] for document in documents]
		#texts = [[word for word in document.split() if word not in stoplist] for document in documents]
		#texts = [[self.unicode_ignore_invalid_char(word) for word in document.lower().split() if word not in stoplist] for document in documents]
		#all_tokens = []
		#for a in texts:
		#	all_tokens.extend(a)
		#print "token extend"
		#tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
		#print "token_once"
		#texts = [[stemmer.stem(word) for word in text if word not in tokens_once] for text in texts]
		#texts = [[word for word in text if word not in tokens_once] for text in texts]
		texts = [[word for word in text] for text in texts]
		print "texts"
		return texts

	def make_corpuses(self):
		texts = self.set_texts()
		dictionary = corpora.Dictionary(texts)
		dictionary.filter_extremes(no_below = 5,no_above = 0.6)
		dictionary.save("./corpus/" + str(self.lda_topics) + "all.dict")
		print "dictionary"
		corpus = [dictionary.doc2bow(text) for text in texts]
		corpora.MmCorpus.serialize("./corpus/" + str(self.lda_topics) + "corpus.mm",corpus)
		print "corpus"
		tfidf = models.TfidfModel(corpus)
		tfidf.save("./corpus/" + str(self.lda_topics) + "tfidf.model")
		print "tf-idf"

	def make_lda(self):
		dictionary = self.set_dictionary()
		corpus = self.set_corpus()
		lda = models.LdaModel(corpus,id2word = dictionary,num_topics = self.lda_topics)
		lda.save("./corpus/lda" + str(self.lda_topics) + "_topics.model")	

	def set_dictionary(self):
		dictionary = corpora.Dictionary.load("./corpus/" + str(self.lda_topics) + "all.dict")
		return dictionary

	def set_corpus(self):
		corpus = corpora.MmCorpus("./corpus/" + str(self.lda_topics) + "corpus.mm")
		return corpus

	def set_tfidf_model(self):
		tfidf = models.TfidfModel.load("./corpus/" + str(self.lda_topics) + "tfidf.model")

	def set_lda(self):
		lda = models.LdaModel.load("./corpus/lda" + str(self.lda_topics) + "_topics.model")
		return lda

	def apply_lda(self):
		lda = self.set_lda()
		stemmer = PorterStemmer()
		dictionary = self.set_dictionary()
		lemmatizer = stem.WordNetLemmatizer()
		sw = StopWords()
		swlist = sw.get_swlist()
		#dirs = os.listdir("./test_data.txt")
		file = open("./test_data_.txt","r")
		page = file.readlines()
		for number,line in enumerate(page):
			f = open("./lda/test/" + str(number) + "_lda.txt","w")
			l = line.split()
			bow = dictionary.doc2bow(l)
			result = dict([(t[0],t[1]) for t in lda[bow]])
			dist = ""
			for i in range(self.lda_topics):
				if i in result:
					dist += str(result[i]) + ","
				else:
					dist += "0.0,"
			print number
			f.write(dist)
			f.close()
		file.close()

if __name__ == "__main__":
	l = Lda()
	#l.make_corpuses()
	#l.make_lda()
	l.apply_lda()
