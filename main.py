from numpy import *
global dict
def buildWDMatrixByList(listFilePath):
    listFile = open(listFilePath,"r")
    wdMatrixList = []
    while(listFile.readable()):
        curLine = listFile.readline()
        if(curLine==""):
            break
        listInt = [int(i) for i in curLine.split(" ")]
        wdMatrixList.append(listInt)
    wdMatrix = mat(wdMatrixList)
    return wdMatrix

def loadDict(path):
    dictFile = open(path,"r")
    global  dict 
    lineCount = 0
    while(dictFile.readable()):
        curLine = dictFile.readline()
        print(lineCount,"finished")
        lineCount+=1
        if(curLine==""):
            break
        lst = curLine.split(" ")
        dict[lst[0]] = int(lst[1])
    return dict

def calcAllDistance(matrix,index):
    
    for i in matrix.shape[0]:
        pass
    return 0    
def calcCosDistance(matrix,vec1Index,vec2Index):
    num = float(matrix[vec1Index]*matrix[vec2Index].T)
    denom = linalg.norm(matrix[vec1Index])*linalg.norm(matrix[vec2Index])
    cos = num /denom
    sim = 0.5 + 0.5 * cos
    return sim

def calcCosDistanceByList(matrix,targetWord,comparedList)
    targetIndex = dict.get(targetWord)
    ans = []
    for i in comparedList:
        comparedIndex = dict.get(i)
        dis = calcCosDistance(matrix,targetIndex,dict[comapredList])
        ans.append(i,comparedIndex,dis)
    return ans

def main():
    matrix =  buildWDMatrixByList("/usr/wikiDataSet/word_ducument5000.matrix")
    U, Sigma, VT = linalg.svd(matrix)
    reducedU = U[0:U.shape[0],0:1000]
    doc = VT[0:1000,0:U.shape[1]]  
    return reducedU,doc  
