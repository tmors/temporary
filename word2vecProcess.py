import multiprocessing

from gensim.models.word2vec import LineSentence, Word2Vec


def generateWord2VecModel(filePath):
    model = Word2Vec(LineSentence(filePath), size=100, window=5, min_count=5, workers=multiprocessing.cpu_count())
    model.save("/usr/dataSet/word2vecModel")
    return model
