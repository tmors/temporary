#coding=utf-8
from commonProcess import *
from lsaProcess import *
from word2vecProcess import *

path = "/usr/dataSet"


def invokeLSAProcess():
    global path
    fileList = loadFile(path)
    for i in fileList:
        print(i)
    global words_dict, articles_dict, words_articles_matrix, wordsWeight
    words_dict,articles_dict,words_articles_matrix  = file2dataSet(fileList)
    wordsWeight = calcWordWeight(words_articles_matrix)
    U, Sigma, VT = LSA(words_articles_matrix)
    buildIndexWordMatrix(words_dict)
    length = Sigma.size
    printAllWordsDistanceAndWeight(words_dict, U, length)


def invokeWord2VecProcess():
    outfile = "/usr/dataSet/wiki/zh.wiki.outfile.model"
    # global path
    filePath = loadFile("/usr/dataSet/wiki/psegCorups.txt")
    # for i in fileList:
    #     print(i)
    model = generateWord2VecModel(filePath)
    model.save(outfile)
    model.save_word2vec_format(outfile + '.vector', binary=False)
    print(model)


if __name__ == "__main__":
    invokeWord2VecProcess()



#svd

#u, sigma, vt = linalg.svd(data)
