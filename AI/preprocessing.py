import pandas as pd
import re
from konlpy.tag import Okt
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
import matplotlib.pyplot as plt
from pprint import pprint
import pickle

data = pd.read_excel('./dataset.xlsx')

X = data['input']
Y = data['output']

X = X.str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","") # 특수문자 제거
stopwords=['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다'] # 불용어

okt = Okt()
x = []
for sentence in X:
    temp_X = []
    temp_X = okt.morphs(sentence, stem=True) # 토큰화
    temp_X = [word for word in temp_X if not word in stopwords] # 불용어 제거
    x.append(temp_X)
X = x
with open('sentences.txt', 'wb') as f:
    pickle.dump(X, f)

max_words = 3000
t = Tokenizer(num_words=max_words) # 상위 3000개의 단어만 보존
t.fit_on_texts(X)
X = t.texts_to_sequences(X)
print(X[:5])

print('리뷰의 최대 길이 :',max(len(l) for l in X))
print('리뷰의 평균 길이 :',sum(map(len, X))/len(X))
plt.hist([len(s) for s in X], bins=50)
plt.xlabel('length of Data')
plt.ylabel('number of Data')
plt.show()

max_len = 15
X = pad_sequences(X, maxlen=max_len)

y = []
for i in range(len(Y)):
    t = [0] * 5
    t[Y[i]-1] = 1
    y.append(t)
Y = y

print(X[:5])
print(Y[:5])

np.save('input.npy', np.array(X))
np.save('output.npy', np.array(Y))
