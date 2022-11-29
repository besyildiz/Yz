# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 09:20:49 2022

@author: ekrem
"""


import pandas as pd
import numpy as np

liste=[1,2,3,"a","b","c"]
df=pd.DataFrame(liste)
df=pd.DataFrame(liste, columns=["Gul"])


data = [['Ali',10],
        ['Ayşe',12],
        ['Mehmet',13]]



df = pd.DataFrame(data,columns=['Ad','Yaş'])

print (df)
##print (data[0,1])
print ("##################")
data = {'Ad':['Ali', 'Ayşe', 'Mehmet'],'Yaş':[10,12,13]}
df = pd.DataFrame(data)
print (df)


df = pd.DataFrame(data,index=['Ogrenci1','Ogrenci2',
 'Ogrenci3'])
print (df)




data=np.random.randint(1,100,size=(6,6))
df=pd.DataFrame(data, columns=["x1","x2","x3","x4","x5","x6"])
print (df.info())

print (df.axes)

print (df.shape)

 
print (df.ndim)
print (df.size)
print (df.values)
print (df.head())

print (df.tail())



 




 



