import os
from pathlib import Path

print(os.path.abspath('.'))  # D:\studyworkspace\seniorsrudy\com\laoshi\senior\study\standard_library\file_test
print(os.path.exists(r'D:\studyworkspace\seniorsrudy'))  # True
print(os.path.isfile(r'D:\studyworkspace\seniorsrudy'))  # False
print(os.path.isdir(r'D:\studyworkspace\seniorsrudy'))  # True
os.path.join('./a/', 'h/f')  # 拼接 不能创建

p1 = Path('.')
print(p1.resolve())  # D:\studyworkspace\seniorsrudy\com\laoshi\senior\study\standard_library\file_test

p2 = Path('./a/b/c')
Path.mkdir(p2, parents=True)
