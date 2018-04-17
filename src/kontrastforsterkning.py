import numpy as np
import matplotlib.pyplot as plt

pause = 1e-4
alpha = .25
steps = 10000
im = plt.imread('lena.png')
im = np.sum(im, 2) / 3
k = 5

def explicitLaplace(img):
    return (img[:-2, 1:-1] +
            img[2:, 1:-1] +
            img[1:-1, :-2] +
            img[1:-1, 2:] -
            4*img[1:-1, 1:-1])

plt.ion()
data = plt.imshow(im, plt.cm.gray)
plt.draw()

lapl0 = explicitLaplace(im)

for i in range(0, steps):
    im[1:-1, 1:-1] += alpha * (explicitLaplace(im) - k * lapl0)

    im[im>1] = 1
    im[im<0] = 0

    im[:, 0] = im[:, 1]
    im[:, -1] = im[:, -2]
    im[0, :] = im[1, :]
    im[-1, :] = im[-2 , :]

    data.set_array(im)
    plt.draw()
    plt.pause(pause)