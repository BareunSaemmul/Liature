# from kor2vec import Kor2Vec
# kor2vec = Kor2Vec.load("../model/path")

# kor2vec.embedding("안녕 아이오아이야 나는 클로바에서 왔어")

# kor2vec.embedding("나는 도라에몽이라고 해 반가워", numpy=True)

# input = kor2vec.to_seqs(["안녕 나는 뽀로로라고 해", "만나서 반가워 뽀로로"], seq_len=4)
# kor2vec.forward(input)

import gensim

model = gensim.models.Word2Vec.load('../../ko.bin')
# result = model.wv.most_similar("땅 미친듯이 흔들림 진짜 뒤질거같아")
# print(model.wv.most_similar("강아지"))
print(model.wv.rank())
# print(result)