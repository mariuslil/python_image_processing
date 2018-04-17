import numpy as np
import matplotlib.pyplot as plt

pause = 1e-4
alpha = .25
steps = 10000
im = plt.imread('lena.png')
im = np.sum(im, 2) / 3

def explicitLaplace(img):
    return (img[:-2, 1:-1] +
            img[2:, 1:-1] +
            img[1:-1, :-2] +
            img[1:-1, 2:] -
            4*img[1:-1, 1:-1])

mask0 = np.zeros(im.shape)
mask0[360:370, 140:150] = 255

mask1 = np.zeros(im.shape)
mask1[245:255, 270:280] = 255

broken = im.copy()
broken[np.where(mask0)] = 1
broken[np.where(mask1)] = 1

imTemp = broken[359:371, 139:151]

for i in range(0, steps):
    imTemp[1:-1, 1:-1] += alpha * explicitLaplace(imTemp)

imTemp = broken[244:256, 269:281]

for i in range(0, steps):
    imTemp[1:-1, 1:-1] += alpha * explicitLaplace(imTemp)

plt.ion()
data = plt.imshow(broken, plt.cm.gray)
data.set_array(broken)
plt.draw()
plt.pause(1000)