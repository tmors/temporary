# 读取数据集文件
import os
from queue import Queue

from langconv import *
import jieba.posseg as pseg

# 1. read the wiki corups and write those to a txt file
# 2. tranfer the traditional chinese to simplified chinese
# 3. split these corups (one article per line)
# 4. 2 branches
# 5. branche A: LSA use the file to build term-document matrix
# 5. branche B: Word2Vec add the file to the model
def loadFile(path):
    # load the dataSet
    q = Queue()
    q.put(path)
    fileList = []
    while (q.qsize() != 0):
        curPath = q.get()
        if (os.path.isdir(curPath)):
            curDir = os.listdir(curPath)
            for i in curDir:
                q.put(curPath + "/" + i)
        else:
            ext = os.path.splitext(curPath)
            if (ext[1] == (".txt")):
                fileList.extend([curPath])
    print("reading file directory compepleted")
    return fileList


def tranditional2simplified(filePath):
    # 转换繁体到简体
    curFile = open(filePath, "r")
    output = open("/usr/dataSet/wiki/simplifiedCorup.txt", 'w')
    i = 0
    while curFile.readable():
        curLine = curFile.readline()
        if(curLine.__eq__("")):
            break
        line = Converter('zh-hans').convert(curLine)
        output.write(line)
        i = i + 1
        if i % 100 == 0:
            print(i, ":finished")
    print(line)
    return

def splitCorups(filePath):
    curFile = open (filePath,'r',encoding="utf-8")
    outFile = open("/usr/dataSet/wiki/psegCorups.txt",'w')
    stopwords = set([line.strip() for line in open('stopwords.txt')])
    i = 0
    while curFile.readable():
        curLine = curFile.readline()
        if(curLine.__eq__("")):
            break
        str = curLine.strip()
        words = pseg.cut(str)
        result = []
        for word,flag in words:
            if (word not in stopwords and word != ' '):
                result.append(word)

        str = " ".join(result)
        outFile.write(str)
        i = i + 1
        if i % 1000 == 0:
            print(i,"finished")

    return

if __name__ == "__main__":
    # tranditional2simplified("/usr/dataSet/wiki/zhwiki.txt")
    splitCorups("/usr/dataSet/wiki/simplifiedCorup.txt")