import re
from konlpy.tag import Okt
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
import pickle
from tensorflow.keras.models import load_model


class Liature_model:
    def __init__(self):
        self.model = load_model('Liature.h5')

    def preprocessing(self, input_data):
        '''
        input_data는 string들이 들어간 리스트. 여러개 가능
        '''

        # input_data = input_data.str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","") # 특수문자 제거
        for i in range(len(input_data)):
            input_data[i] = input_data[i].replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","") # 특수문자 제거
            # datas.append(i.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","")) 


        stopwords=['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다'] # 불용어
        # print(input_data)
        okt = Okt()
        x = []
        for sentence in input_data:
            temp_X = []
            temp_X = okt.morphs(sentence, stem=True) # 토큰화
            temp_X = [word for word in temp_X if not word in stopwords] # 불용어 제거
            x.append(temp_X)
        with open('sentences.txt', 'rb') as f:
            X = pickle.load(f)

        # x.append(x)
        # print(x)
        max_words = 3000
        t = Tokenizer(num_words=max_words) # 상위 3000개의 단어만 보존
        t.fit_on_texts(X)
        x = t.texts_to_sequences(x) # 단어 벡터 길이에 맞게 추가 또는 삭제

        # for i in range(len(x)):
        #     if x[i] == []:
        #         x[i] = 0
        #     else:
        #         x[i] = x[i][0]
        print(x)

        x = pad_sequences(x, maxlen=15)
        print(x)
        return x
    
    def predict(self, *input_data):
        '''
        예측할 데이터를 ,단위로 입력. 입력한 개수만큼 예측 위험도를 리스트로 반환
        '''
        preprocessed_data = self.preprocessing(list(input_data))
        # print(preprocessed_data)
        pred = self.model.predict(preprocessed_data)[0]
        # print(pred)
        answer = []
        for i in pred:
            print((-i).argsort())
            answer.append((-i).argsort()[0]+1)

        return answer


model = Liature_model()
# print(model.predict('포항 지진 안내도 없고 소리나고 흔들렸어요'))
model.predict('포항 지진 안내도 없고 소리나고 흔들렸어요.', 
                '방금 포항 지진났는데 이제 아예 문자도 안올리네', 
                '방금 포항 지진났는데 왜 안 뜨나요ㅠㅠ 한참동안 안 그러다가 갑자기 그래서 진짜 놀랐네요', 
                '포항 방금 지진 맞죠? 재난문자 아직도 안오네요', 
                '포항 방금 지진 발생ㅠㅠ')