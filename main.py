import re
import csv
import numpy as np
import pandas as pd
data = pd.read_excel('data.xlsx',index_col=None,na_values=['NA'],usecols="B")
print('raw_data \n',data.head(1))

# Removing URL in data
data = data['content'] = data['content'].map(lambda x: x.replace('https://',' ').replace('http://',' '))
print('done_remove_url')

# Removing new line in data

data = data['content'] = data['content'].map(lambda x: x.replace('\n',' '))
print('done_remove_newline')
print(data.head(1))

# Removing punctuations
# punc = '\','/','`','*','_','{','}','[',']','(',')','>','#','+','!','$'

for i in data['content']:
    data['content'] = data

print(data.head(10))

# ##segment word
# segment = word_tokenize(data)
# print('done_segment')
#
# # Removing punctuations
# punc= '''!()[]{};:'"\,<>./?@#$%^&*_~'''
# def remove_punc(x):
#     new_list=[]
#     for i in x:
#         if i not in punc:
#             new_list.append(i)
#     return new_list
# segment=remove_punc(segment)
# print('done_remove_punc')
#
# # lower case
# segment = [word.lower() for word in segment]
# print('done_lower_case')
#
# # Removing stopwords
# with open ('vietnamese-stopwords.txt') as stop:
#     stop_word=" ".join(line.strip("\n") for line in stop)
#     def remove_stopwords(segment1):
#         new_words =[]
#         for word in segment1:
#             if word not in stop_word:
#                 new_words.append(word)
#         return new_words
#     segment_final=remove_stopwords(segment)
# segment = None
# print('done_remove_stopword')
#
# # Frequency
# freq=Counter(segment_final)
# most_occour=freq.most_common(50)
# print(most_occour)