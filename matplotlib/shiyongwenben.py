import numpy as np
import matplotlib.pyplot as plt


# mu, sigma = 100, 15
# # x = mu + sigma * np.random.randn(10000)
# #
# # n, bins, patched = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)
# #
# # plt.xlabel('Smarts')
# # plt.ylabel('Probability')
# # plt.title('Histogram of IQ')
# # plt.text(60, 0.025, r'$\mu=100, \sigma=15$')
# # plt.axis([40, 160, 0, 0.03])
# # plt.grid(True)
# # plt.show()


ax = plt.subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw =2)

plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
             arrowprops=dict(facecolor='black', shrink=0.05),)
plt.ylim(-2, 2)
plt.show()