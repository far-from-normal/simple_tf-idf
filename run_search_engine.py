#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from time import time
from tfidf import index, tokenize
        
#%%

# parse comand line arguments
num_arg = len(sys.argv)

if num_arg == 1:
    file_name = 'documents.txt'   
    top_N = 10
    tf_type = 'raw'
elif num_arg == 2:
    file_name = sys.argv[1]  
    top_N = 10
    tf_type = 'raw'
elif num_arg == 3:
    file_name = sys.argv[1]  
    top_N = int(sys.argv[2])
    tf_type = 'raw'
elif num_arg >= 4:
    file_name = sys.argv[1]  
    top_N = int(sys.argv[2])
    tf_type = sys.argv[3]
   
print('\n')
print('Building search engine with the following parameters:')
print('Database: ' + file_name)
print('Top query results: ' + str(top_N))
print('Term frequency type: ' + tf_type)
    
# Build index
start = time()
print('\nNow building index...')

document_index = index(tf_type)
file_object = open(file_name, 'r')
for line in file_object:
    document_index.add_doc_to_index(line)
file_object.close()
document_index.calc_idf()

print('Index completed in ' + str(time() - start) + ' seconds.\n')

# Return queries
while (True):
    try:
        print('Enter search terms separated by spaces: \n')
        # get query string
        queryString = input()
        print('\n')
        # cleaning line\n
        query = tokenize(queryString) 
        # proecced if query string non-empty
        if query:
            # calculating tfidf score
            document_index.print_top_results(file_name, query, top_N)
    # quit on end of file character
    except (EOFError):
        break
sys.exit()
 