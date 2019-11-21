# from konlpy.tag import Twitter
# import pandas as pd
# from collections import Counter

# data = pd.read_csv('dataset.csv', encoding='UTF8')
# s = ''
# for i in data['input']:
#     s += i + ' '

# t = Twitter()
# nouns = t.nouns(s)
# count = Counter(nouns)
# k_l = sorted(list(count.keys()), key=lambda k: count[k], reverse=True)

# for i, k in zip(range(1, len(k_l)+1), k_l):
#     count[k] = i

# print(count)

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import pandas as pd
from pprint import pprint

data = pd.read_csv('dataset.csv', encoding='UTF8')

X = data['input']
Y = data['output']

t = Tokenizer()
print(t)
t.fit_on_texts(X) 
print(t)
sequences = t.texts_to_sequences(X)
pprint(sequences)

w2i = t.word_index
pprint(w2i)

vocab_size = len(w2i)+1
print(vocab_size)