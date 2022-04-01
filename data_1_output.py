import itertools as it
import pandas as pd

'''
输出数据模式
0 | 序号, 
1-9 | 左上, 中上, 右上, 左中, 中中, 右中, 左下, 中下, 右下  # 九宫格
10-25 | 总和/期望值[两者交替]（横下, 横中, 横上, 左斜, 竖左, 竖中, 竖右, 右斜）

6:10000
7:36|8:720|9:360
10:80|11:252|12:108
13:72|14:54|15:180
16:72|17:180|18:119
19:36|20:306|21:1080
22:144|23:1800|24:3600

'''

y = 1
k = 0
li = []
lo = []
lp = []
l_1 = []
l_2 = []
l_3 = []
df = pd.DataFrame([],columns=['左上','中上','右上','左中','中中','右中','左下','中下','右下','总和-横下','期望值-横下','总和-横中','期望值-横中','总和-横上','期望值-横上','总和-左斜','期望值-左斜','总和-竖左','期望值-竖左','总和-竖中','期望值-竖中','总和-竖右','期望值-竖右','总和-右斜','期望值-右斜'],dtype = int)

def expected_value(ev_p):
    ev_o = 0
    if ev_p == 6:
        ev_o = 10000
    elif ev_p == 7:
        ev_o = 36
    elif ev_p == 8:
        ev_o = 720
    elif ev_p == 9:
        ev_o = 360
    elif ev_p == 10:
        ev_o = 80
    elif ev_p == 11:
        ev_o = 252
    elif ev_p == 12:
        ev_o = 108
    elif ev_p == 13:
        ev_o = 72
    elif ev_p == 14:
        ev_o = 54
    elif ev_p == 15:
        ev_o = 180
    elif ev_p == 16:
        ev_o = 72
    elif ev_p == 17:
        ev_o = 180
    elif ev_p == 18:
        ev_o = 119
    elif ev_p == 19:
        ev_o = 36
    elif ev_p == 20:
        ev_o = 306
    elif ev_p == 21:
        ev_o = 1080
    elif ev_p == 22:
        ev_o = 144
    elif ev_p == 23:
        ev_o = 1800
    elif ev_p == 24:
        ev_o = 3600
    return(ev_o)
# 九宫格
t = 0
for i in it.permutations(range(1,10),9): 
    # 0左上、1中上，2右上，3左中，4中中，5右中，6左下，7左中，8右中
    lo = list(i)
    l_1.append(lo)
    t = t + 1
print ('九宫格已完成：' + str(t))

# 合并循环
t = 0
for i in l_1:
    li = i
    # 横下 总和 与 期望值计算
    li.append(i[6] + i[7] + i[8])
    li.append(expected_value(li[-1]))
    # 横中 总和 与 期望值计算
    li.append(i[3] + i[4] + i[5])
    li.append(expected_value(li[-1]))
    # 横上 总和 与 期望值计算
    li.append(i[0] + i[1] + i[2])
    li.append(expected_value(li[-1]))
    # 左斜 总和 与 期望值计算
    li.append(i[0] + i[4] + i[8])
    li.append(expected_value(li[-1]))
    # 竖左 总和 与 期望值计算
    li.append(i[0] + i[3] + i[6])
    li.append(expected_value(li[-1]))
    # 竖中 总和 与 期望值计算
    li.append(i[1] + i[4] + i[7])
    li.append(expected_value(li[-1]))
    # 竖右 总和 与 期望值计算
    li.append(i[2] + i[5] + i[8])
    li.append(expected_value(li[-1]))
    # 右斜 总和 与 期望值计算
    li.append(i[2] + i[4] + i[6])
    li.append(expected_value(li[-1]))
    # print(li)
    df.loc[t] = li
    li = []
    t = t + 1
    if t % 3628 == 0:
        print(df)
        print('已完成' + str( t / 3628 ) + '%')
print(df)
df.to_csv('data.csv')

print("THE END")
