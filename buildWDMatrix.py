from numpy import mat

if __name__ == "__main__":
    path = "/usr/wikiDataSet/pseqSimplifiedCorupsPartition_5000.zh"
    WDFile = open(path, "r")
    articleCount = 5000
    wordDict = {}
    words_articles_matrix = []
    curDocument = 0
    curWord = 0
    limitLine = 2
    while (WDFile.readable()):
        curLine = WDFile.readline()
        if (curLine == ""):
            break

        wordList = curLine.split(" ")
        for i in wordList:
            if (i == ""):
                continue
            if (wordDict.__contains__(i)):
                wordIndex = wordDict.get(i)
                words_articles_matrix[wordIndex][curDocument] = words_articles_matrix[wordIndex][curDocument] + 1
            else:
                words_articles_matrix.append([0 for i in range(0, articleCount)])
                words_articles_matrix[curWord][curDocument] = 1
                wordDict[i] = curWord
                curWord = curWord + 1

        print("read", curDocument, "finished")
        curDocument = curDocument + 1

    outputPath = "/usr/wikiDataSet/word_document.matrix"
    outputFile = open(outputPath, "w")
    sumLine = words_articles_matrix.__len__()
    for i in range(0, words_articles_matrix.__len__()):
        curStr = words_articles_matrix[i]
        outputFile.write(" ".join(str(cur) for cur in curStr) + "\n")
        print("write", i, "/", sumLine, "finished")
    outputFile.close()

    words_articles_matrix = mat(words_articles_matrix)
