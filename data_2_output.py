import itertools as it
import numpy as np
import pandas as pd

'''
计划：
1. 穷举出所有揭露格以及对应数字
    1.1 揭露格（4个不一数字，排序不重复）
    1.2 对应数字（4个不一数字，排序可重复）
'''
print('初始化开始')
t = 0
l_1 = []
l_2 = []
l_3 = []
lo = []
li = []
li_1 = []

df_1 = pd.read_csv('./data/data_1.csv')
print(df_1.shape[0])

'''
for i in range(0,df_1.shape[0]):
    lo = list(df_1.iloc[i])
    del lo[0]
    li_1.append(lo)
print(str(len(li_1)))
'''
def xuanqu(str_input,df_input,number):
    if str_input == 1:
        df_input = df_input.drop(df_input[df_input.A != number].index)
    elif str_input == 2:
        df_input = df_input.drop(df_input[df_input.B != number].index)
    elif str_input == 3:
        df_input = df_input.drop(df_input[df_input.C != number].index)
    elif str_input == 4:
        df_input = df_input.drop(df_input[df_input.D != number].index)
    elif str_input == 5:
        df_input = df_input.drop(df_input[df_input.E != number].index)
    elif str_input == 6:
        df_input = df_input.drop(df_input[df_input.F != number].index)
    elif str_input == 7:
        df_input = df_input.drop(df_input[df_input.G != number].index)
    elif str_input == 8:
        df_input = df_input.drop(df_input[df_input.H != number].index)
    elif str_input == 9:
        df_input = df_input.drop(df_input[df_input.I != number].index)
    return(df_input)



for i in it.combinations(range(1,10),4): 
    # 0左上、1中上，2右上，3左中，4中中，5右中，6左下，7左中，8右中
    lo = list(i)
    l_1.append(lo)
    t = t + 1
lo = []
print ('揭露格已完成：' + str(t))


t = 0
for i in it.permutations(range(1,10),4): 
    # 揭露格的数字
    lo = list(i)
    l_2.append(lo)
    t = t + 1
lo = []
print ('揭露数字已完成：' + str(t))

t = 0
for i in l_1:
    for j in l_2:
        l_3.append(i+j)
        # print(l_3[t])
        t += 1
print('初始化已完成')

t = 0
l_4 = []
l_5 = []
df = pd.DataFrame([],columns=['A','B','C','D','E','F','G','H','A1','B1','C1','D1','E1','F1','G1','H1',],dtype = float)

for i in l_3:
    #位置1-4，数字1-4，输出对应符合条件的可能 both 120 rows
    df_2 = df_1
    df_2 = xuanqu(i[0],df_2,i[4])
    df_2 = xuanqu(i[1],df_2,i[5])
    df_2 = xuanqu(i[2],df_2,i[6])
    df_2 = xuanqu(i[3],df_2,i[7])

    #开始计算期望
    l_4 = i
    for j in range(0,8):
        l = 0
        
        for k in range(0,120):
            m = 11+2*j
            l += df_2.iloc[k,m]
        l = l / 120
        l_4.append(l)
        #print(df)
        #print(i)
        #print(l_4)
    df.loc[t] = l_4
    if t % 3810 == 0:
        print(df)
        print(str(t) + '/ 3841024' + str(t/3810) + '%')
    t += 1

    '''
    df_2.[].isin[i[4]]
    df_2.[xuanqu(i[1])].isin[i[5]]
    df_2.[xuanqu(i[2])].isin[i[6]]
    df_2.[xuanqu(i[3])].isin[i[7]]
    '''
    #print(df_2)
df.to_csv('./data/data_2.csv')        




print(t)
print('done')