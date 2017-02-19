#coding="utf-8"
from lsaProcess import calcWordWeight
from numpy import *

def buildWDMatrixByList(listPath):
    matrixFilePath = listPath
    matrixFile = open(matrixFilePath,"r")
    wdMatrixList = []
    curReadLine = 0
    lineLimitation = 3000
    while(curReadLine < lineLimitation):
        curLine = matrixFile.readline()
        curReadLine += 1
        print(curReadLine,"curLine read")
        if(curLine==""):
            break
        curLineList = curLine.split(" ")
        wdMatrixList.append(curLineList)
    wdMatrix = mat(wdMatrixList)
    return wdMatrixList
if __name__ == "__main__":
    wdMatrixList = buildWDMatrixByList("/usr/wikiDataSet/word_document.matrix")
    wordWeight = calcWordWeight(wdMatrixList)
    curWordWeight = 0
    outputFilePath = "/usr/wikiDataSet/wordWeight.matrix"
    outputFile = open(outputFilePath,"w")
    for i in wordWeight:
        outputFile.write(str(curWordWeight) + " " + str(i) + "\n")
        curWordWeight += 1
        print(curWordWeight,"finished")
    outputFile.close()
