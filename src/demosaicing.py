import numpy as np
import matplotlib.pyplot as plt

pause = 1e-4
alpha = .25
steps = 1000
im = plt.imread('lena.png')
#im = np.sum(im, 2) / 3

def explicitLaplace(img):   #Laplace transformation
    return (img[:-2, 1:-1] +
            img[2:, 1:-1] +
            img[1:-1, :-2] +
            img[1:-1, 2:] -
            4*img[1:-1, 1:-1])

mosaic = np.zeros(u.shape[:2]) # Alloker plass
mosaic[ ::2, ::2] = im[ ::2, ::2, 0] # R-kanal
mosaic[1::2, ::2] = im[1::2, ::2, 1] # G-kanal
mosaic[ ::2, 1::2] = im[ ::2, 1::2, 1] # G-kanal 
mosaic[1::2, 1::2] = im[1::2, 1::2, 2] # B-kanal

demosaic = np.zeros((mosaic.shape[0], mosaic.shape[1], 3)) # Alloker plass
demosaic[ ::2, ::2, 0] = mosaic[ ::2, ::2]   #R
demosaic[1::2, ::2, 1] = mosaic[1::2, ::2]   #G
demosaic[ ::2, 1::2, 1] = mosaic[ ::2, 1::2] #G
demosaic[1::2, 1::2, 2] = mosaic[1::2, 1::2] #B

#mask0 = np.zeros(demosaic.shape[0])
#mask1 = np.zeros(demosaic.shape[1])
#mask2 = np.zeros(demosaic.shape[2])

#mask0[np.where(demosaic[0]) > 1] = 1
#mask1[np.where(demosaic[1]) > 1] = 1
#mask2[np.where(demosaic[2]) > 1] = 1

mask = np.copy(demosaic)
mask[mask > 0] = 1
original = np.copy(demosaic)



for i in range(0, steps):
    demosaic = original * mask + (blured * (1-mask))




plt.ion()
data = plt.imshow(u)
plt.draw()
plt.pause(2)

plt.ion()
data = plt.imshow(mosaic)
plt.draw()
plt.pause(2)

plt.ion()
data = plt.imshow(demosaic)
plt.draw()
plt.pause(2)
