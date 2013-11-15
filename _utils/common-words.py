
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
   m = [[e.lower() for e in re.split('\W+',line)] for line in f]
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
   return set(w_cnter1) & set(w_cnter2)

def remove_stop_words(common, stop_words):
   return common - stop_words
# main method
postdir = '../_posts/'
mdfiles = find_paths(postdir)
mdfiles = [postdir+e for e in mdfiles] # list comprehension to get all the names
d = dict() # add vectors to hashtable
for f in mdfiles:
   vec = gen_words_vector(f)
   d[f] = vec

# numpy 2d distance matrix

g = open('eng-stop-words','r')
g = open('english.stop','r')
stop_wds = set()
[stop_wds.add(e.strip()) for e in g]

# empirically added words
exception_stop_wds = ['ve', 'www','http']
[stop_wds.add(e) for e in exception_stop_wds]

# adding yaml front matter specific top words
yaml_stop_wds = ['post','layout','title','tags','tldr']
[stop_wds.add(e) for e in yaml_stop_wds]

dist_matrix = zeros( (len(mdfiles), len(mdfiles))) 

output_csv = 1
debug = 0

print 'i,j,score'
for i in range(len(mdfiles)):
#for i in range(5):
   for j in range(len(mdfiles)):
   #for j in range(5):
      if i == j:
         # diagonal
         dist_matrix[i,i]=0
         if(output_csv):
            print str(i)+','+str(j)+',0'
         break
      # symmetric matrix
      if(debug):
         print remove_stop_words(distance(d[mdfiles[i]],d[mdfiles[j]]), stop_wds)
      score = len(remove_stop_words(distance(d[mdfiles[i]],d[mdfiles[j]]), stop_wds))/5
      # non-maxima suppression?
      if score > 10:
         out_score = 1
      else:
         out_score = 0
      dist_matrix[i, j] = out_score
      dist_matrix[j, i] = out_score
      if(output_csv):
         print str(i)+','+str(j)+','+str(out_score)
         print str(j)+','+str(i)+','+str(out_score)


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

if(debug):
   # print dist_matrix
   fig,ax = plt.subplots()
   ax.imshow(dist_matrix)
   plt.show() # from 

# use http://bl.ocks.org/mbostock/1308257 as example

