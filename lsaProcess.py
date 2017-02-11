# coding=utf-8
import heapq

import jieba.posseg as pseg
from numpy import *

words_dict = {}
articles_dict = {}
words_articles_matrix = []
index_word_dict = {}
wordsWeight = []
# TODO pos_tagging can be used to extend word
pos_dict = {}


def loadData():
    return [[1, 1, 1, 0, 0],
            [2, 2, 2, 0, 0],
            [3, 3, 3, 0, 0],
            [5, 5, 3, 2, 2],
            [0, 0, 0, 3, 3],
            [0, 0, 0, 6, 6]]


# 读取数据集
def file2dataSet(fileList):
    print("start to read dataSet")
    stopwords = set([line.strip() for line in open('stopwords.txt')])
    partOfSpeech = {};
    fileCount = 8
    words_dict = {}
    articles_dict = {}
    words_cur_location = 0
    articles_cur_location = 0;
    wordsCountPredict = 100000
    articlesCountPredict = 100
    words_articles_matrix = []
    print("init the words_articles_matrix compeleted,wordsCountPredict = ", wordsCountPredict,
          ", articlesCountPredict =", articlesCountPredict)
    # process current article
    for curPath in fileList:
        if (fileCount > 0):
            fileCount = fileCount - 1
        else:
            break
        curFile = open(curPath, "r")

        print("reading current fiel:", curPath)
        article_path = curPath
        articles_dict[article_path] = articles_cur_location
        result = ""
        # set up two dict,(words dict and article dict) to indicate the location of word or article in the 2dim-matrix
        print("reading:" + curPath)
        fileLines = curFile.readlines()
        for line in fileLines:

            str = line.strip()
            words = pseg.cut(str)
            # 去停用词
            for word, flag in words:

                if (word not in stopwords and word != '﻿'):
                    pos_dict[word] = flag
                    if (True):
                        # 去除词性
                        result = result + " " + word + flag  # 去停用词
                        # print(word+flag)
                        getWordIndex = words_dict.get(word)
                        if (getWordIndex is None):
                            words_dict[word] = words_cur_location
                            words_articles_matrix.append([0 for i in range(0, articlesCountPredict)])
                            words_articles_matrix[words_cur_location][articles_cur_location] += 1
                            words_cur_location = words_cur_location + 1
                        else:
                            words_articles_matrix[getWordIndex][articles_cur_location] += 1

        articles_cur_location = articles_cur_location + 1
        print("current file finished:", curPath)
    # 返回词-文章矩阵
    words_articles_matrix = mat(words_articles_matrix)

    return words_dict, articles_dict, words_articles_matrix[0:words_dict.__len__(), 0:articles_dict.__len__()]


# calc word's weight use tf-idf
def calcWordWeight(words_articles_matrix):
    sumOfWordsApperance = sum(words_articles_matrix)
    wordWeight = []
    for i in words_articles_matrix:
        sumOfCurWord = sum(i)
        curWeight = -i * log(sumOfCurWord / sumOfWordsApperance)
        wordWeight.append(sum(curWeight))
    return wordWeight


# SVD return SVD matrix
def LSA(matrix):
    # 进行SVD分解
    U, Sigma, VT = linalg.svd(matrix)
    return U, Sigma, VT


# build index_word_matrix according to word_index_matrix(words_dict)
def buildIndexWordMatrix(words_dict):
    global index_word_dict
    for i in words_dict:
        index = words_dict.get(i)
        index_word_dict[index] = i
    return buildIndexWordMatrix


# get Word By Index from index_word_dict
def getWordByIndex(index):
    word = index_word_dict.get(index)
    return word


# get word weight by word from words_dict
def getWordWeightByWord(word):
    word_index = words_dict.get(word)
    word_frequency = words_articles_matrix[word_index]
    wordWeight = wordsWeight[word_index]
    return wordWeight


# print the word emmbedding
def printWordEmmbedding(U, length):
    cur = 0
    buildIndexWordMatrix(words_dict)
    for i in U:
        word = index_word_dict.get(cur)
        print(word, i[0, 0:length])
        cur = cur + 1
    return


def getDistanceBetweenVectors(curEmbedding, targetEmbedding):
    disEmbedding = curEmbedding - targetEmbedding
    sum = 0
    for i in range(0, disEmbedding.shape[1]):
        sum = sum + disEmbedding[0, i] ** 2
    disPow = sum
    disSqrt = disPow ** 0.5
    return disSqrt


def calcDistanceBetweenTwoWords(sourceWord, targetWord, U, length):
    indexSourceWord = words_dict.get(sourceWord)
    indexTargetWord = words_dict.get(targetWord)
    distance = getDistanceBetweenVectors(U[indexSourceWord][0, 0:length], U[indexTargetWord][0, 0:length])
    return distance


def calcDistanceBetweenTwoIndex(sourceIndex, targetIndex, U, length):
    distance = getDistanceBetweenVectors(U[sourceIndex][0, 0:length], U[targetIndex][0, 0:length])
    return distance


def printAllEmbeddingLimitedBySigma(U, length):
    for i in range(0, U.shape[0]):
        word = index_word_dict.get(i)
        print(word, U[i][0, 0:length])
    return


def calcDistanceByWord(word, U, length, top=5):
    index = words_dict.get(word)
    curEmbedding = U[index]
    distanceListDict = []
    for i in range(0, U.shape[0]):
        if index == i:
            continue
        dis = getDistanceBetweenVectors(curEmbedding[0, 0:length], U[i][0, 0:length])
        curDict = {}
        curDict['word'] = index_word_dict.get(i)
        curDict['distance'] = dis
        curDict['weight'] = wordsWeight[i]
        distanceListDict.append(curDict)
    # we will find the nearest point in the distanceList
    sortedListByDistance = heapq.nsmallest(top, distanceListDict, key=lambda s: s['distance'])
    sortedListByWeight = heapq.nlargest(top, sortedListByDistance, key=lambda s: s['weight'])
    return sortedListByWeight


# print the distances and weight of every word with others to explain effects of LSA
def printAllWordsDistanceAndWeight(words_dict, U, length, top=5):
    for word in words_dict:
        sortedList = calcDistanceByWord(word, U, length, top)
        print(word, sortedList)
    return


def search():
    return
