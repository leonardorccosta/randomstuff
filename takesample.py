# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 08:41:32 2019

@author: HP
"""

#listar os nomes dos arquivos
from os import listdir
path = 'C:/machine-learning/Henrique/'
def find_csv_filenames( path , suffix=".xlsx" ):
    filenames = listdir(path)
    return [ filename for filename in filenames if filename.endswith( suffix )]
filenames = find_csv_filenames(path)
filenames

import pandas as pd
import random
import gc

df = pd.DataFrame()

for i in range(len(filenames)):
  filename = path+filenames[i]
  importado = pd.read_excel(filename).fillna(method='ffill')
  
  n = (len(importado) - 1) #número de linhas no arquivo
  s = 5 #Numero de linhas para tirar de cada dataset
  
  if len(importado) > 10:
      pular = sorted(random.sample(range(1,n+1),s)) #tirar o index
      df = df.append(importado.iloc[pular], ignore_index=True)
      print('arquivo:',i+1, 'de',len(filenames) ,'| tamanho: ', importado.shape,'| df', df.shape)
  else: print('arquivo:', i+1, 'de', len(filenames) , 'pulado por conter poucas linhas')
    
  del [importado] #Deletar o nome do dataframe 
  gc.collect() #deletar o dataframe

df.to_csv("C:/machine-learning/Henrique/exemplo2000.csv")