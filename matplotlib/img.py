import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('bb.jpg', True)

# print(img)

imgplot = plt.imshow(img)

lum_img = img[:, :, 0]
plt.imshow(lum_img)

plt.imshow(lum_img, cmap='hot')

imgplot = plt.imshow(lum_img)
imgplot.set_cmap('nipy_spectral')


plt.colorbar()
imgplot = plt.imshow(lum_img, clim=(0.0, 0.7))
plt.hist(lum_img.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')

fig = plt.figure()
a = fig.add_subplot(1, 2, 1)
imgplot = plt.imshow(lum_img)
a.set_title('Before')
plt.colorbar(ticks=[0.1, 0.3, 0.5, 0.7], orientation='horizontal')

a = fig.add_subplot(1, 2, 2)
imgplot = plt.imshow(lum_img)
imgplot.set_clim(0.1, 0.7)
a.set_title('After')
plt.colorbar(ticks=[0.1, 0.3, 0.5, 0.7], orientation='horizontal')



from PIL import  Image
# 降低图像像素
img = Image.open('bb.jpg')
img.thumbnail((64,64), Image.ANTIALIAS)


# imgplot = plt.imshow(img)
# imgplot = plt.imshow(img, interpolation='nearest')

#模糊处理
imgplot = plt.imshow(img, interpolation='bicubic')


plt.show()
