#coding="utf-8"
from lsaProcess import calcWordWeight
from numpy import *
if "__name__" == "__main__":
	matrixFilePath = "/usr/wikiDataSet/word_document.matrix"
	matrixFile = open(matrixFilePath,"r")
	wdMatrixList = []
	curReadLine = 0
	while(matrixFile.readable()):
		curLine = matrixFile.readline()
		curReadLine += 1
		print(curReadLine,"curLine read")
		if(curLine==""):
			break
		curLineList = curLine.split(" ")
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
		
		
