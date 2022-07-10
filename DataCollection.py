import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
files=os.listdir(r'Uber/Dataset/')
path=r'.Uber/Dataset/'
final=pd.DataFrame()
for file in files:
    fileloc=path+file
    print(fileloc)
    try:
        df=pd.read_csv(fileloc,encoding='utf-8')
    except:
        df=pd.read_csv(fileloc,encoding='cp1252')

    final=pd.concat([df,final])
