#coding=utf-8
from numpy import *
import os.path
from multiprocessing import Queue
import jieba
import jieba.posseg as pseg
import scipy
def loadData():
    return [[1, 1, 1, 0, 0],
            [2, 2, 2, 0, 0],
            [3, 3, 3, 0, 0],
            [5, 5, 3, 2, 2],
            [0, 0, 0, 3, 3],
            [0, 0, 0, 6, 6]]
#读取数据集文件
def loadFile(path):
    #load the dataSet
    q = Queue()
    q.put(path)
    fileList = []
    while(q.qsize()!=0):
        curPath = q.get()
        if(os.path.isdir(curPath)):
            curDir = os.listdir(curPath)
            for i in curDir:
                q.put(curPath+ "/" + i)
        else:
            ext = os.path.splitext(curPath)
            if(ext[1]==(".txt")):
                fileList.extend([curPath])
    print("reading file directory compepleted")
    return fileList
#读取数据集
def file2dataSet(fileList):
    print("start to read dataSet")
    stopwords = set([line.strip() for line in open('stopwords.txt')])
    partOfSpeech = {};
    fileCount = 3
    words_dict = {}
    articles_dict = {}
    words_cur_location = 0
    articles_cur_location = 0;
    wordsCountPredict = 100000
    articlesCountPredict = 100
    words_articles_matrix = [[0 for i in range(articlesCountPredict)] for j in range(wordsCountPredict)]
    print("init the words_articles_matrix compeleted,wordsCountPredict = ",wordsCountPredict,", articlesCountPredict =", articlesCountPredict)
    #process current article
    for curPath in fileList:
        curFile = open(curPath,"r")
        print("reading current fiel:",curPath)
        article_path = curPath
        articles_dict[article_path] = articles_cur_location

        fileLines = curFile.readlines()
        result = ""
        if (fileCount > 0):
            fileCount = fileCount - 1
        else:
            return
        #set up two dict,(words dict and article dict) to indicate the location of word or article in the 2dim-matrix
        print("reading:"+ curPath)
        for line in fileLines:

            str = line.strip()
            words = pseg.cut(str)
            #去停用词
            for word,flag in words:
                if(word not in stopwords and word != '﻿'):
                    if(True):
                        #去除词性
                        result = result +" " +  word + flag   #去停用词
                        #print(word+flag)
                        getWordIndex = words_dict.get(word)
                        if(getWordIndex is None):
                            words_dict[word]=words_cur_location
                            words_articles_matrix[words_cur_location][articles_cur_location] += 1
                            words_cur_location = words_cur_location + 1
                        else:
                            words_articles_matrix[getWordIndex][articles_cur_location] += 1

        articles_cur_location = articles_cur_location + 1
        print("current file finished:",curPath)
    #返回词-文章矩阵
    words_articles_matrix = mat(words_articles_matrix)
    return words_dict,articles_dict,words_articles_matrix[0:words_dict.__len__(),0:articles_dict.__len__()]



def LSA(matrix):
    #进行SVD分解
    return


if __name__=="__main__":
    path = "/usr/dataSet"
    fileList = loadFile(path)
    for i in fileList:
        print (i)
    words_dict,articles_dict,words_articles_matrix  = file2dataSet(fileList)
    print(words_articles_matrix)

#svd

#u, sigma, vt = linalg.svd(data)
