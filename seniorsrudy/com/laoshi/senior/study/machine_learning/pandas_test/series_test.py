import pandas as pd

# obj1 = pd.Series([4, 5, -6, 7])
#
# # 0    4
# # 1    5
# # 2   -6
# # 3    7   自带从0开始的索引
# # dtype: int64
# print(obj1)
# # int64
# print(obj1.dtype)
# # RangeIndex(start=0, stop=4, step=1) 索引从0开始，到4结束，每次加1
# print(obj1.index)
# # [ 4  5 -6  7]
# print(obj1.values)

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

