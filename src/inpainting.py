from defVar import *    #Import variabels and packages


mask = np.zeros(im.shape)
mask[200:250, 0:200] = 255
mask[360:380, 140:185] = 255
mask[400:500, 270:345] = 255

broken = im.copy()
broken[np.where(mask)] = 1




while True:
    plt.ion()
    data = plt.imshow(broken, plt.cm.gray)
    data.set_array(broken)
    plt.draw()
    plt.pause(pause)



#blur.blurring(broken, alpha, steps, pause, 'd')  #Send to blur function to do the inpainting