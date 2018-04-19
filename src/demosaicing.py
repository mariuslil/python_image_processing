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

def blur(ima):
    #for i in range(0, 1):
    ima[1:-1, 1:-1, 0] += alpha * explicitLaplace(ima[:, :, 0])
    ima[1:-1, 1:-1, 1] += alpha * explicitLaplace(ima[:, :, 1])
    ima[1:-1, 1:-1, 2] += alpha * explicitLaplace(ima[:, :, 2])
    
    ima[:, 0, :] = ima[:, 1, :]
    ima[:, -1, :] = ima[:, -2, :]
    ima[0, :, :] = ima[1, :, :]
    ima[-1, :, :] = ima[-2 , :, :]
    return ima

plt.ion()
data = plt.imshow(im)
plt.draw()
plt.pause(1)

mosaic = np.zeros(im.shape[:2]) # Alloker plass
mosaic[ ::2, ::2] = im[ ::2, ::2, 0] # R-kanal
mosaic[1::2, ::2] = im[1::2, ::2, 1] # G-kanal
mosaic[ ::2, 1::2] = im[ ::2, 1::2, 1] # G-kanal 
mosaic[1::2, 1::2] = im[1::2, 1::2, 2] # B-kanal

demosaic = np.zeros((mosaic.shape[0], mosaic.shape[1], 3)) # Alloker plass
demosaic[ ::2, ::2, 0] = mosaic[ ::2, ::2]   #R
demosaic[1::2, ::2, 1] = mosaic[1::2, ::2]   #G
demosaic[ ::2, 1::2, 1] = mosaic[ ::2, 1::2] #G
demosaic[1::2, 1::2, 2] = mosaic[1::2, 1::2] #B

mask = np.copy(demosaic)
mask[mask > 0] = 1
original = np.copy(demosaic)

plt.ion()
data = plt.imshow(demosaic)
plt.draw()
plt.pause(1)

for i in range(0, steps):
    blurred = blur(demosaic)
    demosaic = original * mask + (blurred * (1 - mask))
    
    data.set_array(demosaic)
    plt.draw()
    plt.pause(pause)