# -*- coding: utf-8 -*-
import sys
import numpy as np
import statistics
from statistics import mean
import csv

#データの標準正規化

a = np.loadtxt('test.csv',delimiter=',')
print(a[0][0])
def standardization_p(l):
    l_mean = statistics.mean(l)
    l_pstdev = statistics.pstdev(l)
    return np.array([(i - l_mean) / l_pstdev for i in l])
print(mean(standardization_p(a[0])))
print(statistics.pstdev(standardization_p(a[0])))
norm = np.empty((0,len(a[0])),float)
print(norm)
for i in range(len(a)):
    norm = np.append(norm,np.array([standardization_p(a[i])]), axis=0)
    print(standardization_p(a[i]))
print(norm)
with open('test1.csv','w') as f:
    writer = csv.writer(f)
    writer.writerows(norm)
