import jieba
import os
from gensim import corpora, models, similarities


train_set = []
root_dir = "/home/zhounan/corpus/sogou"



def load_train_set(root_dir):
    for parent, dirs, files in os.walk(root_dir):
        for filename in files:
            load_single_file(os.path.join(parent, filename))


def load_single_file(path):
    f = open(path)
    raw_text = f.read()
    word_list = list(jieba.cut(raw_text, cut_all = False))
    train_set.append(word_list)


def generate_model():
    lda_dict = corpora.Dictionary(train_set)
    count = 0
    for wid in lda_dict:
	print wid, lda_dict[wid].encode("utf-8")
        count += 1
    
	"""
	print len(lda_dict)
    lda_dict.save("total_dict")
    lda_dict.save_as_text("total_dict.txt")
    corpus = [lda_dict.doc2bow(text) for text in train_set]
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]
    tfidf.save("total_tfidf")
    tfidf.initialize
    #lda = models.LdaModel(corpus_tfidf, id2word=lda_dict, num_topics = 10)
    #corpus_lda = lda[corpus]
    #for i in range(0, 10):
    #    print lda.print_topic(i)
	"""


load_train_set(root_dir)
#load_single_file("/home/zhounan/corpus/sogou/C000008/1571.txt_utf8")
generate_model()
#total_dict = corpora.Dictionary.load("total_dict")
