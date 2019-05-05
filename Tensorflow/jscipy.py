import numpy as np
import matplotlib.pyplot as plt
from imageio import imread

# x = np.arange(0, 3*np.pi, 0.1)
# y_sin = np.sin(x)
# y_cos = np.cos(x)
#
# plt.subplot(2, 1,1)
#
# plt.plot(x, y_sin)
# plt.title('Sine')
#
# plt.subplot(2, 1, 2)
# plt.plot(x, y_cos)
# plt.title('Cosine')
#
# plt.xlabel('x axis label')
# plt.ylabel('y axis label')
# plt.title('Sine and Cosine')
# plt.legend(['Sine', 'Cosine'])
# plt.show()


img = imread('1.png')
plt.subplot(1,2,1)
plt.imshow(img)

plt.subplot(1,2,2)
plt.imshow(np.uint8(img))

plt.show()
