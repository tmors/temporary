import sys

if __name__ == "__main__":
    input, output = sys.argv[1:3]
    inputFile = open(input,"r")
    outputFile = open(output,"w")
    lineCount = 50000
    for i in range(0,lineCount):
        curLine = inputFile.readline()
        outputFile.write(curLine)
    outputFile.close()
    inputFile.close()
