#coding="utf-8"
from lsaProcess import calcWordWeight
from numpy import *
if "__name__" == "__main__":
	matrixFilePath = "/usr/wikiDataSet/word_document.matrix"
	matrixFile = open(matrixFile,"r")
	wdMatrixList = []
	while(matrixFile.readable()):
		curLine = matrix.readline()
		if(curLine==""):
			break
		curLineList = curLine.splited(" ")
		wdMatrixList.append(curLineList)
	wdMatrix = mat(wdMatrixList)		
	wordWeight = calcWordWeight(wdMatrix)
	curWordWeight = 0
	outputFilePath = "/usr/wikiDataSet/wordWeight.matrix"
	outputFile = open(outputFilePath,"w")
	for i in wordWeight:
		curWordWeight += 1
		outputFile.write(i + "\n")
		print(curWordWeight,"finished")
	outputFile.close()
		
		
