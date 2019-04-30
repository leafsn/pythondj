import matplotlib.pyplot as plt
import  numpy as np

# plt.plot([1,2,3,4])
#x轴为[1,2,3,4]
plt.plot([1,2,3,4],
         [1,4,9,16])

#红色圆圈绘制
plt.plot([1,2,3,4],
         [1,3,5,18], 'ro')
#x为0-6    y轴为0-20    [xmin, xmax, ymin, ymax]
plt.axis([0,6,
          0,20])

plt.figure()
t = np.arange(0., 5., 0.2)
plt.plot(t, t,    'r--',
         t, t**2, 'bs',
         t, t**3, 'g^')



x = np.linspace(-1, 1,50)

y1 = 2*x+1
plt.figure()
plt.plot(x,y1)

y2 = x**2
plt.figure()
plt.plot(x, y2)

y2 = x**2
plt.figure(num=5, figsize=(4,4))
plt.plot(x, y1)
plt.plot(x, y2, color='red', linewidth=1.0,linestyle='--')
plt.show()


## 柱状图
x = np.array([1,2,3,4,5,6,7,8])
y = np.array([3,5,7,6,2,6,10,15])

plt.plot(x,y,'r')
plt.plot(x,y,'g', lw=5)

x = np.array([1,2,3,4,5,6,7,8])
y = np.array([13,14,15,16,17,19,43,20])
plt.bar(x,y,0.2,alpha=1,color='b')
plt.show()

for i in range(0, 15):
    dateOne = np.zeros([2])
    dateOne[0] = i
    dateOne[1] = i
    y = np.zeros([2])
    y[0] = 10
    y[1] = 20
    plt.plot(dateOne, y, 'r', lw=8)
plt.show()

## 设置坐标轴
x = np.linspace(-1, 1, 50)
y1 = 2 * x + 1
y2 = x**2

plt.figure()
plt.plot(x, y1)
plt.plot(x, y2, color = 'red', linewidth = 1.0, linestyle = '--')

#设置坐标轴的取值范围
plt.xlim((-1, 2))
plt.ylim((0, 2))

#设置坐标轴的label
plt.xlabel(u'这是x轴', fontproperties='SimHei', fontsize=14)
plt.ylabel(u'这是y轴', fontproperties='SimHei', fontsize=14)

#设置坐标轴刻度
plt.xticks(np.linspace(-1, 1, 5))

#获取当前的坐标轴
ax = plt.gca()

#设置有边框和上边框
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

## 设置x轴为下边框
ax.xaxis.set_ticks_position('bottom')
## 设置y轴为做边框
ax.yaxis.set_ticks_position('left')

## 设置x轴，y轴在0,0的位置
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', -1))

## 设置坐标点文字样式
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor = 'green', edgecolor ='none', alpha= 0.5))


plt.show()




