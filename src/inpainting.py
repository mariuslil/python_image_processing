import numpy as np
import matplotlib.pyplot as plt

pause = 1e-4
alpha = .25
steps = 100
im = plt.imread('lena.png')

def explicitLaplace(img):   #Laplace transformation
    return (img[:-2, 1:-1] +
            img[2:, 1:-1] +
            img[1:-1, :-2] +
            img[1:-1, 2:] -
            4*img[1:-1, 1:-1])

def inpaint(ima):
    plt.ion()
    data = plt.imshow(broken)
    plt.draw()
    plt.pause(2)
    
    for i in range(0, steps):
        ima[1:-1, 1:-1] += alpha * explicitLaplace(ima)
        data.set_array(broken)
        plt.draw()
        plt.pause(pause)

mask0 = np.zeros(im.shape)
mask0[360:370, 140:150] = 255

mask1 = np.zeros(im.shape)
mask1[245:255, 270:280] = 255

broken = im.copy()
broken[np.where(mask0)] = 1
broken[np.where(mask1)] = 1

inpaint(broken[359:371, 139:151])
inpaint(broken[244:256, 269:281])