import numpy as np
import matplotlib.pyplot as plt

pause = 1e-4
alpha = .25
steps = 100
im = plt.imread('lena.png')
im = np.sum(im, 2) / 3

def explicitLaplace(img):   #Laplace transformation
    return (img[:-2, 1:-1] +
            img[2:, 1:-1] +
            img[1:-1, :-2] +
            img[1:-1, 2:] -
            4*img[1:-1, 1:-1])

def inpaint(ima, colour):
    if colour:  #Colour
        plt.ion()
        data = plt.imshow(broken)
        plt.draw()
        plt.waitforbuttonpress()
    
    else:   #Greyscale
        plt.ion()
        data = plt.imshow(broken, plt.cm.gray)
        plt.draw()
        plt.waitforbuttonpress()
    
    for i in range(0, steps):
        ima[1:-1, 1:-1] += alpha * explicitLaplace(ima)
        data.set_array(broken)
        plt.draw()
        plt.pause(pause)
    plt.waitforbuttonpress()


mask0 = np.zeros(im.shape)
mask0[360:370, 140:150] = 255

mask1 = np.zeros(im.shape)
mask1[245:255, 270:280] = 255

broken = im.copy()
broken[np.where(mask0)] = 1
broken[np.where(mask1)] = 1

inpaint(broken[359:371, 139:151], False)
inpaint(broken[244:256, 269:281], False)

im = plt.imread('lena.png')

broken = im.copy()
broken[np.where(mask0)] = 1
broken[np.where(mask1)] = 1

inpaint(broken[359:371, 139:151], True)
inpaint(broken[244:256, 269:281], True)