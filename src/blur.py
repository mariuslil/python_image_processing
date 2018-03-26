from defVar import *    #Import variabels and packages

def explicitLaplace(im):
    return (im[:-2, 1:-1] +
            im[2:, 1:-1] +
            im[1:-1, :-2] +
            im[1:-1, 2:] -
            4*im[1:-1, 1:-1])

def blurring(im, alpha, steps, pause, boundary):

    plt.ion()
    data = plt.imshow(im, plt.cm.gray)
    plt.draw()

    for i in range(0, steps):
        im[1:-1, 1:-1] += alpha * explicitLaplace(im)
        if boundary == 'n':    # Neumann boundary
            im[:, 0] = im[:, 1]
            im[:, -1] = im[:, -2]
            im[0, :] = im[1, :]
            im[-1, :] = im[-2 , :]
        
        data.set_array(im)
        plt.draw()
        plt.pause(pause)
        

#blurring(im, alpha, steps, pause, 'n')