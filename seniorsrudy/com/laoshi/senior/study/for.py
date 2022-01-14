# for 迭代变量 in 可迭代对象：
#     代码块
shengXiao = '鼠牛虎兔龙蛇马羊猴鸡狗猪'
for cz in shengXiao:
    print(cz)

# range()
for i in range(12):
    print(i)

for year in range(2000, 2021):
    print("%s 年的生肖是 %s" % (year, shengXiao[year % 12]))

# while 表达式：
#     代码块

# 计算从1到10所有偶数的平方
aList = []
for i in range(1, 11):
    if i % 2 == 0:
        aList.append(i * i)
print(aList)

bList = [i * i for i in range(1, 11) if i % 2 == 0]
print(bList)
