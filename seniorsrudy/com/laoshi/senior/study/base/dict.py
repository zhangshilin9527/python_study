# 字典  有点类似于java中的map
dictA = {}
print(type(dictA))

dictB = {'a': 1, 'b': 2}
print(dictB)
dictB['c'] = 3
print(dictB)

shengXiao = '鼠牛虎兔龙蛇马羊猴鸡狗猪'
xingZuo = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座', u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')
days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

cz_num = {}
for i in shengXiao:
    cz_num[i] = 0

z_num = {}
for i in xingZuo:
    z_num[i] = 0
print(cz_num)
print(z_num)

zNum = {i: 0 for i in xingZuo}
print(zNum)


while True:
    year = int(input("请输入年份"))
    month = int(input("请输入月份"))
    day = int(input("请输入日期"))
    for dayNum in range(len(days)):
        if days[dayNum] >= (month, day):
            print(xingZuo[dayNum])
            cz_num[shengXiao[year % 12]] += 1
            z_num[xingZuo[dayNum]] += 1
            break
        elif month == 12 and day > 23:
            print(xingZuo[0])
            cz_num[shengXiao[year % 12]] += 1
            z_num[xingZuo[dayNum]] += 1
            break

    for each_key in cz_num.keys():
        print("生肖 %s 有 %d个" % (each_key, cz_num[each_key]))

    for each_key in z_num.keys():
        print("星座 %s 有 %d个" % (each_key, z_num[each_key]))
