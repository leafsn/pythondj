import matplotlib.pyplot as plt
import  numpy as np

# plt.plot([1,2,3,4])
#x轴为[1,2,3,4]
plt.plot([1,2,3,4], [1,4,9,16])

#红色圆圈绘制
plt.plot([1,2,3,4], [1,3,5,18], 'ro')
#x为0-6    y轴为0-20    [xmin, xmax, ymin, ymax]
plt.axis([0,6,0,20])

t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')


t2 = t**2
plt.figure(num=3, figsize=(8,5))
l1, = plt.plot(t, t2, label='up')
l2, =plt.plot(t, t2**2,color='red', linewidth=2, linestyle='--', label='down')

plt.legend(handles=[l1,l2], labels=['aaa','bbb'], loc='best')

plt.xlim((-1,2))
plt.ylim((0, 2))
plt.xlabel('I am x')
plt.ylabel('I am y')

new_ticks = np.linspace(-1,2,5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2,-1.8,-1,1.22,3],[r'$one$',r'$two$',r'$three$',r'$four$',r'$five$'])
ax = plt.gca()

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',-1))
ax.spines['left'].set_position(('data',0))

#添加注解
x0 = 0.3
y0 = x0**2
plt.scatter(x0,y0,s=50,color='b')
plt.plot([x0,x0], [y0,0],'k--',lw=2.5)
plt.annotate(r'$2x+1=%s$' % y0, xy=(x0,y0), xycoords='data',xytext=(+30, -30),textcoords='offset points',
             fontsize=16,arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))

plt.text(-3.3,3,r'$This is the some text, \mu\sigma_i\alpha_t$',fontdict={'size':16,'color':'r'})




x = np.linspace(-3, 3, 50)
y = 0.1*x

plt.figure()
# 在 plt 2.0.2 或更高的版本中, 设置 zorder 给 plot 在 z 轴方向排序
plt.plot(x, y, linewidth=10, zorder=1)
plt.ylim(-2, 2)
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor='white', edgecolor='None',alpha=0.7,zorder=3))




### 散点图

n = 1024
x = np.random.normal(0,1,n)
y = np.random.normal(0,1,n)

t = np.arctan2(y,x)
plt.scatter(x,y,s=75,c=t,alpha=0.5)

plt.xlim(-1.5,1.5)
plt.ylim(-1.5,1.5)

plt.xticks(())
plt.yticks(())

# plt.ylabel('some number')

plt.show()


## 条形图
import matplotlib.pyplot as plt
import numpy as np

n = 12
x = np.arange(n)
y1 = (1-x/float(n))*np.random.uniform(0.5, 1.0,n)
y2 = (x-x/float(n))*np.random.uniform(0.5, 1.0,n)

plt.bar(x, +y1, facecolor='#999999', edgecolor='white')
plt.bar(x, -y2, facecolor="#ff9999", edgecolor='white')

plt.xlim(-5, n)
plt.xticks(())
plt.ylim(-1.25, 1.25)
plt.yticks(())

for x,y in zip(x, y1):
    plt.text(x+0.1, y+0.05,'%.2f'%y,ha='center', va='bottom')

# for x,y in zip(x, y2):
#     plt.text(x+0.4, -y-0.05,'%.2f'%y,ha='center',va='top')


plt.show()
