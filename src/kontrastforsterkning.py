import numpy as np
import matplotlib.pyplot as plt

pause = 1e-4
alpha = .25
steps = 100
im = plt.imread('lena.png')
k = 5

def explicitLaplace(img):   #Laplace transformation
    return (img[:-2, 1:-1] +
            img[2:, 1:-1] +
            img[1:-1, :-2] +
            img[1:-1, 2:] -
            4*img[1:-1, 1:-1])

def contrast(ima, colour):
    if colour:
        plt.ion()
        data = plt.imshow(ima)
        plt.draw()

    else:
        ima = np.sum(im, 2) / 3
        plt.ion()
        data = plt.imshow(ima, plt.cm.gray)
        plt.draw()

    lapl0 = explicitLaplace(ima) #Laplace for original image

    for i in range(0, steps):   #Increace contrast
        ima[1:-1, 1:-1] += alpha * (explicitLaplace(ima) - k * lapl0)
        #clamps values
        ima[ima>1] = 1
        ima[ima<0] = 0
        #Neuman boundary
        ima[:, 0] = ima[:, 1]
        ima[:, -1] = ima[:, -2]
        ima[0, :] = ima[1, :]
        ima[-1, :] = ima[-2 , :]

        data.set_array(ima)
        plt.draw()
        plt.pause(pause)

contrast(im, False)
contrast(im, True)