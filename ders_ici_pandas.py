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


d1=np.random.randint(0,100,size=10)
d2=np.random.randint(0,100,size=10)
d3=np.random.randint(0,100,size=10)
d4=np.random.randint(0,100,size=10)

dict={"seri1":d1,"seri2":d2,"seri3":d3,"seri4":d4}

df=pd.DataFrame(dict)

rastgele1=np.random.randint(1,20,size=(4,3))
rastgele2=np.random.randint(20,40,size=(4,3))

df1=pd.DataFrame(rastgele1,columns=["x","y","z"])
df2=pd.DataFrame(rastgele2,columns=["x","y","z"])

df=pd.concat([df1,df2])
df

df=pd.concat([df1,df2],ignore_index=True, join="inner")
df

df=pd.concat([df1,df2],ignore_index=True)
df


sol = pd.DataFrame({ "anahtar": ["A0", "A1", "A2", "A3"], 
                    "X": ["X0", "X1", "X2", "X3"], 
                    "Y": ["Y0", "Y1", "Y2", "Y3"], })

sag = pd.DataFrame({
 "anahtar": ["A0", "A1", "A2", "A3"],
 "Z": ["Z0", "Z1", "Z2", "Z3"],
 "T": ["T0", "T1", "T2", "T3"],
 })


birlesim = pd.merge(sol, sag,on="anahtar")
birlesim

birlesim = pd.merge(sol, sag,on="anahtar",how="right")
birlesim

df.to_csv("verim.csv")
df.to_json("verim.json")























