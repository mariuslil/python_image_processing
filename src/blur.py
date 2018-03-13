import numpy as np
import matplotlib.pyplot as plt

def explicitLaplace(im):
    return (im[:-2, 1:-1] +
            im[2:, 1:-1] +
            im[1:-1, :-2] +
            im[1:-1, 2:] -
            4*im[1:-1, 1:-1])

def blurring(im, alpha, steps, pause):
    for i in range(0, steps):
        im[1:-1, 1:-1] += alpha * explicitLaplace(im)
        
        im[:, 0] = im[:, 1]      # Neumann boundary
        im[:, -1] = im[:, -2]
        im[0, :] = im[1, :]
        im[-1, :] = im[-2 , :]
        
        data.set_array(im)
        plt.draw()
        plt.pause(pause)
        

alpha = .25
im = plt.imread('lena.png')
im = np.sum(im, 2) / 3.

plt.ion()
data = plt.imshow(im, plt.cm.gray)
plt.draw()

blurring(im, alpha, 10000, 1e-4)