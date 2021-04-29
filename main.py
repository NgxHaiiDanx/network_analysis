import pandas as pd
# !pip install vncorenlp
data = pd.read_excel('data.xlsx',index_col=None,na_values=['NA'],usecols="B")
print('raw_data \n',data.head(5))

# Removing URL in data
data = data['content'] = data['content'].map(lambda x: x.replace('https://',' ').replace('http://',' '))
print('done_remove_url')
print(data.head(5))

# Removing new line in data
data = data['content'] = data['content'].map(lambda x: x.replace('\n',' '))
print('done_remove_newline')
print(data.head(5))

# Removing punctuations
# punc = ['\','/',"`",'*',"_","{","}","[","]","(",")",">","+","!","$"]
punc = """[\/`?*_={}[]()<>+!%$^@]"""
for i in punc:
    print(i)
for j in data['content']:
    for i in j:
        data = j.replace(i,'')
print(data.head(10))

# removing stop words
with open('vietnamese-stopword.txt') as f:
    sw=("".join(line.strip("\n") for line in f))
print(sw)
