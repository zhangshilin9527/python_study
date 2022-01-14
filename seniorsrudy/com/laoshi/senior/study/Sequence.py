# 序列 它的成员都是有序排列，并且可以通过下标偏移量访问到他的一个或者几个成员
# 1.字符串

shengXiao = '鼠牛虎兔龙蛇马羊猴鸡狗猪'

year = 2021
print(shengXiao[year % 12])

# 输出第一个
print(shengXiao[0])
# 输出前四个
print(shengXiao[0:4])
# 输出最后一个
print(shengXiao[-1])

# in not in
print('狗' in shengXiao)
print('狗' not in shengXiao)

# 重复 *
print(shengXiao * 3)

# 2.元组  存储内容不可变更

a = (1, 3, 5, 7, 9)

b = 4
# 取出小于4的元素
print(filter(lambda x: x < b, a))
# 取出小于4的元素 并列出
print(list(filter(lambda x: x < b, a)))

# 小于4的个数
print(len(list(filter(lambda x: x < b, a))))

xingZuo = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座', u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')
days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

(month, day) = (3, 1)
lenth = len(list(filter(lambda x: x < (month, day), days))) % 12
print(xingZuo[2])

# filter取出xxxxx

# 3.列表  存储内容可变更