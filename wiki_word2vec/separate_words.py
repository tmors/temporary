__author__ = 'huang'

import logging
import os
import sys

import jieba

if __name__=='__main__':

    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)

    if len(sys.argv) < 3:
        print(globals()['__doc__'] %locals())
        sys.exit(1)

    inp, outp = sys.argv[1:3]
    space = ' '

    output = open(outp, 'w')
    # inp = open('wiki.cn.text.jian', 'r')
    inp = open(inp, 'r')
    i = 1
    for line in inp.readlines():
        if line == '\n' or line == "":
            continue
        seg_list = jieba.cut(line)
        str = space.join(seg_list)
        output.write(str)
        if i % 1000 == 0:
            print(i, "finished")
    output.close()
