
import re
from collections import Counter
import os
from numpy import *
import numpy as np
import matplotlib.pyplot as plt

def gen_words_vector(path):
   f = open(path,'r')
   # two approaches
   # 1) analyze the md files
   #  * will contain all irelevant preamble. will have to remove layout, post,title,tldr,tags
   # 2) analyze html files
   #  * the content might be clearer
   #  * but will also have to remove all the header, footer, navigation, disqus crap anyway
   
   # choice, go with analyzing md files
   
   # splits on all non-alphanumeric characters
   m = [[e for e in re.split('\W+',line)] for line in f]
   # flattens list and removes all empty strings
   
   m = [item for sublist in m for item in sublist if len(item) > 0]
   
   # generates a dict<K,V> where K is hashable-obj in our case a string, and V is an int
   cnt = Counter(m)
   return cnt

# data struct. 2d distance matrix
# data struct. 1d matrix of vectors (words)

def find_paths(postdir):
   mdfiles = [name for name in os.listdir(postdir) if os.path.isfile(os.path.join(postdir,name))]
   return mdfiles

def distance(w_cnter1,w_cnter2):
   return len(set(w_cnter1) & set(w_cnter2))


# main method
postdir = '../_posts/'
mdfiles = find_paths(postdir)
mdfiles = [postdir+e for e in mdfiles] # list comprehension to get all the names
d = dict() # add vectors to hashtable
for f in mdfiles:
   vec = gen_words_vector(f)
   d[f] = vec

# numpy 2d distance matrix
dist_matrix = zeros( (len(mdfiles), len(mdfiles))) 

print 'i,j,score'
for i in range(len(mdfiles)):
   for j in range(len(mdfiles)):
      if i == j:
         # diagonal
         print str(i)+','+str(j)+',0'
         break
      # symmetric matrix
      print str(i)+','+str(j)+','+str(distance(d[mdfiles[i]],d[mdfiles[j]]))
      print str(j)+','+str(i)+','+str(distance(d[mdfiles[i]],d[mdfiles[j]]))
      dist_matrix[i, j] = distance(d[mdfiles[i]],d[mdfiles[j]])

# lower triangle
#for i in range(len(mdfiles)):
#   for j in range(len(mdfiles)):
#      if i == j:
#         break
#      print str(i)+','+str(j)+','+str(distance(d[mdfiles[i]],d[mdfiles[j]]))
#      dist_matrix[i, j] = distance(d[mdfiles[i]],d[mdfiles[j]])



#d = dist_matrix.tolist()
#for l in d:
#   for e in l:
#      print str(e)+'\t',
#   print

set_printoptions(threshold='nan')
# print dist_matrix
fig,ax = plt.subplots()
ax.imshow(dist_matrix)
#plt.show()
# from 
g = open('eng-stop-words','r')
stop_wds = set()
[stop_wds.add(e.strip()) for e in g]

# TODO
# 1. remove the common words from the diagram
# 2. create a d3.js visualization
# use http://bl.ocks.org/mbostock/1308257 as example

