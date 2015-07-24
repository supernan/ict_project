#import plsa as pl
import os


words_dict = dict()
total_words = 0

def load_word_count(path):
	f = open(path)
	count = 0
	for line in f:
		parts = line.strip().split('\t')
		word_id = int(count)
		word_tf = float(parts[2])
		words_dict[word_id] = word_tf
		print str(word_id), parts[1]
		count += 1
load_word_count("total_dict.txt")
