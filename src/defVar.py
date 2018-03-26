import numpy as np
import matplotlib.pyplot as plt

pause = 1e-4
alpha = .25
steps = 10000
im = plt.imread('lena.png')
im = np.sum(im, 2) / 3