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

def blurring(ima, alpha, steps, pause, colour):
    if colour:  #Colour blur
        plt.ion()
        data = plt.imshow(ima)
        plt.draw()    
    
    else:   #Grayscale blur
        ima = np.sum(im, 2) / 3
        plt.ion()
        data = plt.imshow(ima, plt.cm.gray)
        plt.draw()

    for i in range(0, steps):
        ima[1:-1, 1:-1] += alpha * explicitLaplace(ima)
        # Neumann boundary
        ima[:, 0] = ima[:, 1]
        ima[:, -1] = ima[:, -2]
        ima[0, :] = ima[1, :]
        ima[-1, :] = ima[-2 , :]
        
        data.set_array(ima)
        plt.draw()
        plt.pause(pause)

blurring(im, alpha, steps, pause, False)
blurring(im, alpha, steps, pause, True)