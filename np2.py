# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 09:17:08 2022

@author: ekrem
"""

import numpy as np
x=np.random.randint(0,101,([10,3]))

x.max()
x.min()


x.sum()
x.sum(axis=0)
x.sum(axis=1)


x.max(axis=0)
x.max(axis=1)
x.min(axis=0)
x.min(axis=1)


x.mean()
x.mean(axis=0)
x.mean(axis=1)



