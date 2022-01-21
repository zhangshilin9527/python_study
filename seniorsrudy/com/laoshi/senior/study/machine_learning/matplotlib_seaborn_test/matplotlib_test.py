import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

# 绘制简单的曲线
# 以1,2,3为横坐标，以4,7,6为纵坐标的曲线，过点（1,4），（2,7），（3,6）
plt.plot([1, 2, 3], [4, 7, 6])
plt.show()  # 在pycharm中显示图像

x = np.linspace(-np.pi, np.pi, 100)  # 在-3.14和3.14中间取100个值
y = np.sin(x)
plt.plot(x, y)
plt.show()

x2 = np.linspace(-np.pi * 2, np.pi * 2, 100)  # 从-2π到2π中间去100个数
plt.figure(10, dpi=50)  # 图像名称为figure10  清晰度50 dpi代表精细度，dpi越大文件越大，杂志要300以上
for i in range(1, 5):
    y2 = np.sin(x2 / i)
    plt.plot(x2, y2)
plt.show()
# 绘制直方图
plt.figure(1, dpi=100)
data1 = [1, 1, 1, 3, 3, 3, 5, 5, 6, 7, 9]
plt.hist(data1)  # 绘制直方图
plt.show()

# 绘制散点图
x = np.arange(1, 10)  # [1 2 3 4 5 6 7 8 9]
y = x
plt.scatter(x, y, c='r', marker='o')  # plt.scatter()绘制散点图 c='r' 表示点是红色，marker='o'表示点用圆体现
plt.show()

# 读取文件 绘制图表
csv1 = pd.read_csv('./aaa.csv')
# print(csv1.head())  #显示头五行
csv1.plot(kind='scatter', x='x', y='y')  # scatter表示散点图
plt.show()

csv2 = pd.read_csv('./aaa.csv')
# 设置样式
sns.set(style='white', color_codes=True)
# 绘制散点图
sns.jointplot(x='x', y='y', data=csv2, size=5)
# displot绘制曲线
sns.distplot(csv2['x'])
plt.show()

csv3 = pd.read_csv('./aaa.csv')
sns.set(style='white', color_codes=True)
# FacetGrid 一般绘制函数
# hue 对csv中的'virginca'一列彩色显示分类 0/1/2
# plt.scatter 绘制散点图
# add_legend() 显示分类的描述信息
sns.FacetGrid(csv3, hue='virginca', size=5).map(plt.scatter, 'x', 'y').add_legend()
# sns.FacetGrid(csv3, hue='virginca', size=5).map(plt.scatter, 'setosa', 'vsesicolor').add_legend()
plt.show()
