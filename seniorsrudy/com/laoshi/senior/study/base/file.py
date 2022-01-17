# python中的文件包括txt exe 网址 程序间通讯等
# open()
# read
# readline
# seek 文件内移动
# write
# close
# 将小说的主要任务记录在文件中
# file1 = open("name.txt", 'w')
# file1.write("诸葛亮")
# file1.close()
#
# file2 = open("name.txt")
# print(file2.read())
# file2.close()
#
# file3 = open("name.txt", 'a')
# file3.write("刘备")
# file3.close()

file4 = open("name.txt")
print("当前指针的位置是 %s" % file4.tell())
print(file4.read(1))
# seek两个参数 第一个表示迁移量，第二个表示位置：0表示从开头开始偏移， 1表示从当前位置， 2表示从结尾
# file4.seek(0)
print("当前指针的位置是 %s" % file4.tell())
# file4.seek(1, 1)
print(file4.read())
file4.close()
