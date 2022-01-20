# Dataframe  类似于处理电子 表格，适用于多维数组
import pandas as pd
from numpy import nan as NA

# 第一种方式：字典放列表，字典的key为列，行为数字索引
data = {'city': ['shanghai', 'shanghai', 'shanghai', 'beijing', 'beijing'],
        'year': [2016, 2017, 2018, 2017, 2018],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
df1 = pd.DataFrame(data)

#        city  year  pop
# 0  shanghai  2016  1.5
# 1  shanghai  2017  1.7
# 2  shanghai  2018  3.6
# 3   beijing  2017  2.4
# 4   beijing  2018  2.9
print(df1)
# 0    shanghai
# 1    shanghai
# 2    shanghai
# 3     beijing
# 4     beijing
print(df1.city)
# shanghai
print(df1.city[0])

df2 = pd.DataFrame(data, columns=['year', 'city', 'pop'])  # 按照 'year','city','pop'排序
#    year      city  pop
# 0  2016  shanghai  1.5
# 1  2017  shanghai  1.7
# 2  2018  shanghai  3.6
# 3  2017   beijing  2.4
# 4  2018   beijing  2.9
print(df2)
# 0    2016
# 1    2017
# 2    2018
# 3    2017
# 4    2018
# Name: year, dtype: int64
print(df2.year)
# 0    2016
# 1    2017
# 2    2018
# 3    2017
# 4    2018
# Name: year, dtype: int64
print(df2['year'])

df2['new'] = 100  # 增加一列'new'，并将值赋予100
#    year      city  pop  new
# 0  2016  shanghai  1.5  100
# 1  2017  shanghai  1.7  100
# 2  2018  shanghai  3.6  100
# 3  2017   beijing  2.4  100
# 4  2018   beijing  2.9  100
print(df2)

df2['cap'] = df2.city == 'beijing'  # 增加'cap'列，并判断它是不是beijing

#    year      city  pop  new    cap
# 0  2016  shanghai  1.5  100  False
# 1  2017  shanghai  1.7  100  False
# 2  2018  shanghai  3.6  100  False
# 3  2017   beijing  2.4  100   True
# 4  2018   beijing  2.9  100   True
print(df2)

# 第二种方式：字典里面放字段，第一个字典key是列，第二个字典key是行
pop = {'beijing': {2008: 1.5, 2009: 2.0},
       'shanghai': {2008: 2.0, 2009: 3.6}}

df3 = pd.DataFrame(pop)
#       beijing  shanghai
# 2008      1.5       2.0
# 2009      2.0       3.6
print(df3)
#           2008  2009
# beijing    1.5   2.0
# shanghai   2.0   3.6
print(df3.T)  # 将行和列调换

# 若放多个列表，则多个列表分别为第n行，索引从0开始
df4 = pd.DataFrame([[1, 2, 3],
                    [2, NA, NA],
                    [NA, NA, NA]])
#      0    1    2
# 0  1.0  2.0  3.0
# 1  2.0  NaN  NaN
# 2  NaN  NaN  NaN
print(df4)
df4[4] = NA  # 将第4列值设置为NA
#      0    1    2   4
# 0  1.0  2.0  3.0 NaN
# 1  2.0  NaN  NaN NaN
# 2  NaN  NaN  NaN NaN
print(df4)
#      0    1    2   4
# 0  1.0  2.0  3.0 NaN
# 1  2.0  NaN  NaN NaN
print(df4.dropna(axis=1, how='all'))  # 将全是（how='all'）NaN的一列（xis=1）删除
#      0    1    2    4
# 0  1.0  2.0  3.0  0.0
# 1  2.0  0.0  0.0  0.0
# 2  0.0  0.0  0.0  0.0
print(df4.fillna(0))  # 将df4的副本NaN值全部默认为0，其实df4并未修改
#      0    1    2   4
# 0  1.0  2.0  3.0 NaN
# 1  2.0  NaN  NaN NaN
# 2  NaN  NaN  NaN NaN
print(df4)
df4.fillna(0, inplace=True)  # 将df4的NaN值全部默认为0
print(df4)
