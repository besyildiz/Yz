import pandas as pd
import numpy as np

data = ["Merve","Yusuf", "Ayşe","Zehra"]

s1 = pd.Series(data)
print(s1)

s2=pd.Series([1,2,3,4])
print(s2)
print(s2[0])

dizi = np.array(['b','i','l','i','ş','i','m'])
s3=pd.Series(dizi)
print(s3)