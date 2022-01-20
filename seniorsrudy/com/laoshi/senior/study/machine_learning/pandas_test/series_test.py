from numpy import nan as NA
import pandas as pd

# series适用于一维数组,参数为列表

obj1 = pd.Series([4, 5, -6, 7])

# 0    4
# 1    5
# 2   -6
# 3    7   自带从0开始的索引
# dtype: int64
print(obj1)
# int64
print(obj1.dtype)
# RangeIndex(start=0, stop=4, step=1) 索引从0开始，到4结束，每次加1
print(obj1.index)
# [ 4  5 -6  7]
print(obj1.values)

obj2 = pd.Series([4, 5, 3, 6], index=['a', 'b', 2, 'd'])
# a    4
# b    5
# 2    3
# d    6
# dtype: int64
print(obj2)
obj2[2] = 9  # 令obj2[2] = 9
# a    4
# b    5
# 2    9
# d    6
# dtype: int64
print(obj2)
# True
print('b' in obj2)  # 索引'b'是否属于obj2

data = {'北京': 100, '上海': 200, '广州': 300, '深圳': 400}
obj3 = pd.Series(data)

# 北京    100
# 上海    200
# 广州    300
# 深圳    400
# dtype: int64
print(obj3)

obj3.index = ['bj', 'sh', 'gz', 'sz']
# bj    100
# sh    200
# gz    300
# sz    400
# dtype: int64
print(obj3)

obj4 = pd.Series([4, 5, 6, -7], index=['a', 'c', 'd', 'b'])
# a    4
# c    5
# d    6
# b   -7
# dtype: int64
print(obj4)
obj5 = obj4.reindex(index=['a', 'b', 'c', 'd', 'e'], fill_value=0)  # 重新排序，并且增加一个'e'索引,fill_value=0  并将增加的索引默认值设为0
# a    4
# b   -7
# c    5
# d    6
# e    0
# dtype: int64
print(obj5)

obj6 = pd.Series(['blue', 'yellow', 'green'], index=[0, 2, 4])
# 0      blue
# 2    yellow
# 4     green
# dtype: object
print(obj6)
# 0      blue
# 1      blue
# 2    yellow
# 3    yellow
# 4     green
# 5     green
# dtype: object
# 对obj6进行排序，索引从0-5，（method='ffill'）将默认值设置成与前面值一样，（method='bfill'）将默认值设置成与后面值一样
print(obj6.reindex(index=range(6), method='ffill'))


# 删除 nan值(空值)
obj7 = pd.Series([1, NA, 2])
# 0    1.0
# 1    NaN
# 2    2.0
# dtype: float64
print(obj7)
# 0    1.0
# 2    2.0
# dtype: float64
print(obj7.dropna())  # 删除空值
