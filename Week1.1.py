# -*- coding: utf-8 -*-
"""
Created on Fri May 05 16:41:40 2017
All code can be implement in Python2
@author: szsyz
"""

from pylab import *
from scipy.cluster.vq import *
list1 = [88.0,74.0,96.0,85.0]
list2 = [92.0,99.0,95.0,94.0]
list3 = [91.0,87.0,99.0,95.0]
list4 = [78.0,99.0,97.0,81.0]
list5 = [88.0,78.0,98.0,84.0]
list6 = [100.0,95.0,100.0,92.0]
data = vstack((list1,list2,list3,list4,list5,list6))
centroids,_ = kmeans(data,2)
result,_= vq(data,centroids)
print result
