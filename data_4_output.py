import itertools as it
import numpy as np
import pandas as pd

df = pd.read_csv('./data/data_3.csv')
df = df.drop(['PID'],axis=1)
#print(df)

t = 0
l_j = []

for i in it.combinations(range(1,10),4): 
    # 0左上、1中上，2右上，3左中，4中中，5右中，6左下，7左中，8右中
    l = list(i)
    l_j.append(l)
    t = t + 1
l = []
#print ('揭露格已完成：' + str(t))

for i in l_j:
    df_1 = df.loc[(df.A == i[0]) & (df.B == i[1]) & (df.C == i[2]) & (df.D == i[3])]
    sum_n = list(df.loc[:,'ex_v'])
    sum_v = np.sum(sum_n)
    print(sum_v)



