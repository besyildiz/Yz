# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 09:36:11 2022

@author: ekrem
"""

import matplotlib.pyplot as plt
import numpy as np


#liste = [4, 5, 8, 3, 2, 7]
#plt.plot(liste)
#plt.show()



#dizi = np.arange(30)
#plt.plot(dizi)
#plt.show()


#x=np.arange(25)
#y=x**2+1
#plt.plot(x,y)
#plt.show()


#x = [5, 2, 7]
#y = [1, 6, 10]
#plt.plot(x, y)
#plt.title('Çizgi Grafik')
#plt.ylabel('Y Ekseni')
#plt.xlabel('X Ekseni')
#plt.show()



#x = np.arange(0,10)
#y0 = np.random.randint(10,14,10)
#y1 = np.random.randint(14,18,10)
#y2 = np.random.randint(18,22,10)
#plt.plot(x,y0)
#plt.plot(x,y1)
#plt.plot(x,y2)
#plt.show()


diller = ['C', 'C++', 'Python', 'Java']
oranlar = [25,30,35,40]
plt.xlabel("Diller")
plt.ylabel("Oranlar")
plt.bar(diller,oranlar)
plt.show()






























