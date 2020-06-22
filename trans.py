# -*- coding: utf-8 -*-
import sys
import numpy as np

#転置するプログラム。コマンド引数でファイル指定

fin = open(sys.argv[1], "r")
fout = open(sys.argv[2], "w")
for line in np.array([s.strip('\n').split(',') for s in fin]).T:
    fout.write("  ".join(line) + "\n")
fin.close()
fout.close()
