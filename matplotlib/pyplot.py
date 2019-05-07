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


plt.ylabel('some number')
plt.show()

