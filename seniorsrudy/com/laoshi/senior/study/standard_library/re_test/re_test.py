import re

#  . 匹配任意的单个字符
#  ^ 匹配以什么作为开头
#  $ 匹配以什么作为结尾
#  * 匹配前面的字符出现0次-n次
#  + 匹配前面的字符出现1次-n次
#  ? 匹配前面的字符出现0次-1次
#  {} 匹配前面的字符的次数  a{4} a出现4次  a{4,6}a出现4-6次
#  [] 匹配括号内的出现的字符  c[bcd]t  可以匹配 cbt cct cdt
#  |  选择左边或者右边
#  \d 匹配内容为一串数字
#  \D 匹配内容不包含数字
#  \s 匹配内容为字符串
#  () 进行分组

# ^$表示这一行为空行
# .*?  不适用贪婪模式 只匹配第一个
# sub() 替换 与java中的replace功能一样


# r 不进行转义

a = re.compile('a')
a.match('a')  # 比较
print(a.match('a'))  # <re.Match object; span=(0, 1), match='a'>  匹配0-1共1个字符
print(a.match('b'))  # None

abc = re.compile('abc')
print(abc.match('abc'))  # <re.Match object; span=(0, 3), match='abc'> 匹配0-3 共3个字符
print(abc.match('a1bc'))  # None
print(abc.match('abcd'))  # <re.Match object; span=(0, 3), match='abc'> 匹配0-3 共3个字符

ab = re.compile('ab*')  # *
print(ab.match('abcd'))  # <re.Match object; span=(0, 2), match='ab'> 匹配0-2 共2个字符
print(ab.match('abbbbbc'))  # <re.Match object; span=(0, 6), match='abbbbb'> 匹配0-6 共6个字符

# r 不进行转义

# match 精确匹配
p = re.compile(r'(\d+)-(\d+)-(\d+)')
print(p.match('2018-05-10'))  # <re.Match object; span=(0, 10), match='2018-05-10'>
# group 分组
print(p.match('2018-05-10').group())  # 2018-05-10
print(p.match('2018-05-10').group(1))  # 2018
print(p.match('2018-05-10').group(2))  # 05
print(p.match('2018-05-10').group(3))  # 10
print(p.match('2018-05-10').groups())  # ('2018', '05', '10')
year, month, day = p.match('2018-05-10').groups()
print(year)  # 2018
print(month)  # 05
print(day)  # 10

# match精确匹配    search 模糊匹配
print(p.match('aa2018-05-10bb'))  # None
print(p.search('aa2018-05-10bb'))  # <re.Match object; span=(2, 12), match='2018-05-10'>

# sub()
phone = '138-1234-6666 @ 手机号'
# 三个参数 第一个匹配规则，第二个替换的事情，第三个元数据
p2 = re.sub(r'@.*$', '', phone)  # 将138-1234-6666 @ 手机号  中@后面的字符替换成空
print(p2)  # 138-1234-6666
p3 = re.sub(r'\D', '', p2)  # 将 138-1234-6666中的-去掉
print(p3)  # 13812346666
