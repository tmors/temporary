#coding=utf-8
from lsaProcess import *


if __name__=="__main__":
    path = "/usr/dataSet"
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

# TODO word2vec part


#svd

#u, sigma, vt = linalg.svd(data)
