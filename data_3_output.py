import itertools as it
import numpy as np
import pandas as pd

df = pd.read_csv('./data/data_2.csv')
df.insert(df.shape[1],'ex_n','')
df.insert(df.shape[1],'ex_v',0.0)

df[['A','B','C','D','E','F','G','H']] = df[['A','B','C','D','E','F','G','H']].astype('int32')

t = 0
t_100 = df.shape[0] // 100

for i in range(0,df.shape[0]):
    l = list(df.loc[i])
    del l[0]
    #[1, 2, 3, 4, 1, 2, 3, 4, 861.5, 230.8, 10000.0, 109.1, 113.2, 114.5, 131.8, 131.8, '', 0.0]
    max_number = max(l[8:15])
    if l[8] == max_number:
        df.loc[i,'ex_n'] = 'A'
        df.loc[i,'ex_v'] = l[8]
    elif l[9] == max_number:
        df.loc[i,'ex_n'] = 'B'
        df.loc[i,'ex_v'] = l[9]
    elif l[10] == max_number:
        df.loc[i,'ex_n'] = 'C'
        df.loc[i,'ex_v'] = l[10]
    elif l[11] == max_number:
        df.loc[i,'ex_n'] = 'D'
        df.loc[i,'ex_v'] = l[11]
    elif l[12] == max_number:
        df.loc[i,'ex_n'] = 'E'
        df.loc[i,'ex_v'] = l[12]
    elif l[13] == max_number:
        df.loc[i,'ex_n'] = 'F'
        df.loc[i,'ex_v'] = l[13]
    elif l[14] == max_number:
        df.loc[i,'ex_n'] = 'G'
        df.loc[i,'ex_v'] = l[14]
    elif l[15] == max_number:
        df.loc[i,'ex_n'] = 'H'
        df.loc[i,'ex_v'] = l[15]
    if t % t_100 ==0:
        print (str(t // t_100) + '%')
    t += 1

df = df.drop(['PID','A1','B1','C1','D1','E1','F1','G1','H1'],axis=1)
    
df.to_csv('./data/data_3.csv')
