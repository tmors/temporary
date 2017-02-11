from gensim.models.word2vec import LineSentence, Word2Vec


def generateWord2VecModel(fileList):
    for i in fileList:
        sentences = LineSentence(i)
    model = Word2Vec(sentences, size=100, window=5, min_count=5, workers=4)
    model.save("/usr/dataSet/word2vecModel")
    return model
