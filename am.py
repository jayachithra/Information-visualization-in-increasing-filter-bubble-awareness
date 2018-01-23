# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 14:36:25 2018

@author: Jaya
"""


# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 20:10:05 2017

@author: Jaya
"""


# coding: utf-8

# # BotNet Lab!
# Group 8: Azqa Nadeem, Jaya Chithra



from collections import OrderedDict
import itertools
import pandas as pd

import plotly
import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd
import math
import json
import pyfpgrowth
from pymining import itemmining

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import matplotlib


def count(src):   #data preprocessing
     
   #extract genres from csv
   with open(src) as f:
       sourceips = f.readlines()    
       #genres = sourceips.strip().split(' ')[1]
   sourceips = [x.strip().split('\t')[1] for x in sourceips]
   
   #find distinct genres   
   ips = truecount(sourceips)
        
   #sort the genres based on their frequency (from most frequent to least) 
   sorted_x = OrderedDict(sorted(ips.items(), key=lambda x: x[1], reverse=True))   
   sorted_x = dict(sorted_x)
   
   
   print("Genres , Frequencies")
   print("---------------------")
   for key, value in sorted_x.items():
       print(key,value)
   
    #Find and print 10 most frequent values   
#   x = itertools.islice(sorted_x.items(), 0, 20)         
#   for key, value in x:
#       print(key , value)

   #plotscatter(sorted_x) 
   #barchart(sorted_x)
       
def countmv(src):   # #data preprocessing
   #extract genres from csv  
   df = pd.read_csv(src) 
   saved_column = df['genres']
   data = tuple(saved_column)
   
   #extract individual genre combinations
   splitdata = tuple()
   for x in data:
     if '|' in x:
      x = x.split('|') 
      splitdata = splitdata + (tuple(x),)
     else:
      splitdata = splitdata + (tuple([x]),)
   
   
   
   #find frequent genres - Frequent Item Set Mining
   relim_input = itemmining.get_relim_input(splitdata)
   report = itemmining.relim(relim_input, min_support=4)
   #print(report)
   
   
           
   #sort the genres based on their frequency (from most frequent to least) 
   sorted_x = OrderedDict(sorted(report.items(), key=lambda x: x[1], reverse=True))   
   sorted_x = dict(sorted_x)
   #print(sorted_x)
   sorted_x = {tuple(k) : v for k, v in sorted_x.items()}
   #sorted_x.update((tuple(k), v) for k, v in sorted_x.items())
   #print(sorted_x)
   
   #print(len(sorted_x))
   
#   print("Genres , Frequencies")
#   print("---------------------")
#   for key, value in sorted_x.items():
       #print(key,value)
   
   # Find and print 10 most frequent values
   genres, values = [], []   
   x = itertools.islice(sorted_x.items(), 0, 10)  
   #print(x)       
   for key, value in x:
       #print(key , value)
       genres.append(key)
       values.append(value)
   
   genres = listoftuplestolistofstrings(genres) 
    
   barchart(genres,values) 
 
#Actual count of each item   
def truecount(sourceips):    
    c = {}
    for x in sourceips:
       c[x] = 0
    for x in sourceips:
       c[x] += 1   
    return c   


def listoftuplestolistofstrings(x):
    
    genres = []
    
    for genre_combi in x:
      if len(genre_combi) > 1:
          genre_name = " "
          for genre in genre_combi:
              genre_name +=  str(genre)
              genre_name += ", "
          genre_name = genre_name[:-2]
          genres.append(genre_name)
      else:
          for genre in genre_combi:
              genres.append(str(genre))
    
    return genres


    
def barchart(x,y):
   
  
  y_pos = np.arange(len(x))
   
  plt.barh(y_pos, y, align='center', alpha=0.2)
  plt.yticks(y_pos, x)
  plt.ylabel('genres')
  plt.xlabel('frequencies')
  
  plt.show()
  
  
    
if __name__ == "__main__":
    #src = 'normalize_normal.csv'
    src = 'genres.txt'
    #
    #print('------------Music------------')
    #count(src)
    
    src = 'movies.csv'
    #Count without using FREQUENT
    #print('------------Movies------------')
    countmv(src)
    
  
   


