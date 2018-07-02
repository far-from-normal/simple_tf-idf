#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import math
from heapq import nlargest
from operator import itemgetter
from time import time

def tokenize(line):
    words = re.sub('[^A-Za-z0-9]+', ' ', line.strip().lower()).split(' ')
    if '' in words:
        words.remove('')
    return words

class index:
    def __init__(self, tf_type):
        self.doc_id_ = 0
        self.tf_type_ = tf_type
        self.vocab_ = dict()
        self.doc_ = dict()
        self.tf_ = dict()
        self.idf_ = dict()
        self.doc_count_ = dict()
        self.score_ = dict()
        self.topScores_ = None
        self.top_docs_ = None
        
    '''term frequency (tf) definitions:
    https://en.wikipedia.org/wiki/Tf–idf'''
        
    def tf_raw(self, document_words):
        self.tf_[self.doc_id_] = dict((x, document_words.count(x)) for x in set(document_words) )
        return None
    
    def tf_bool(self, document_words):
        self.tf_[self.doc_id_] = dict((x, int(x in document_words)) for x in set(document_words) )
        return None
        
    def tf_norm(self, document_words):
        self.tf_[self.doc_id_] = dict((x, document_words.count(x)/len(document_words)) for x in set(document_words) )  
        return None
        
    def tf_log(self, document_words):
        self.tf_raw(document_words)
        for term in self.tf_[self.doc_id_]:
            self.tf_[self.doc_id_][term] = math.log( 1.0 + self.tf_[self.doc_id_][term] )
        return None

    def tf_aug(self, document_words):
        self.tf_raw(document_words)
        max_tf = max(self.tf_[self.doc_id_].values())
        for term in self.tf_[self.doc_id_]:
            self.tf_[self.doc_id_][term] = 0.5 + 0.5 * ( self.tf_[self.doc_id_][term] / max_tf )
        return None
        
    def get_tf(self, document_words):
        if self.tf_type_ == 'raw':
            self.tf_raw(document_words)
        elif self.tf_type_ == 'bool':
            self.tf_bool(document_words)
        elif self.tf_type_ == 'norm':
            self.tf_norm(document_words)
        elif self.tf_type_ == 'log':
            self.tf_log(document_words)
        elif self.tf_type_ == 'aug':
            self.tf_aug(document_words)
        else:
            self.tf_raw(document_words)        
        return None
    
    def add_term_to_doc_count(self, document_words):
        for term in set(document_words):
            if term in self.doc_count_:
                self.doc_count_[term] += 1
            else:
                self.doc_count_[term] = 1     
        return None
        
    def add_doc_to_index(self, line):
        document_words = tokenize(line)
        self.doc_[self.doc_id_] = document_words
        self.get_tf(document_words)
        self.add_term_to_doc_count(document_words)
        self.doc_id_ += 1
        return None
    
    def calc_idf(self):
        for term in self.doc_count_:
            self.idf_[term] = math.log( len(self.doc_) / ( 1.0 + self.doc_count_[term] ) )
        return None
    
    def tfidf_score(self, query): 
        self.score_ = dict()
        for doc_id in self.tf_:
            self.score_[doc_id] = 0.0
            for term in query:
                if (term in self.idf_) and (term in self.tf_[doc_id]):
                    self.score_[doc_id] += self.tf_[doc_id][term] * self.idf_[term]
        return None
    
    def top_tfidf_results(self, query, top_N):
        self.tfidf_score(query)
        self.topScores_ = dict(nlargest(top_N, self.score_.items(), key=itemgetter(1)))
        return None
    
    def print_top_results(self, file_name, query, top_N):
        start = time()
        self.top_tfidf_results(query, top_N)
        self.top_docs_ = dict()
        file_object = open(file_name, 'r')
        for num, line in enumerate(file_object):
            if num in self.topScores_.keys():
                self.top_docs_[line] = self.topScores_[num]
        doc_ctr = 0
        for doc, score in sorted(self.top_docs_.items(), key=itemgetter(1), reverse=True):
            if score > 0.0:
                doc_ctr += 1
                print(str(doc_ctr).rjust(3) + '. (' + str(score)[:5] + ')' + '\t' + doc)
        print('\n Top ' + str(top_N) + ' results requested. Only ' + str(doc_ctr) + ' documents match the search criteria. Search completed in ' + str(time()-start) + ' seconds.\n')
        return None