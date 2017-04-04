import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colors


def plot(X,Y,pred_func):
    # determine canvas borders
    mins = np.amin(X,0); 
    mins = mins - 0.1*np.abs(mins);
    maxs = np.amax(X,0); 
    maxs = maxs + 0.1*maxs;
    ## generate dense grid
    xs,ys = np.meshgrid(np.linspace(mins[0,0],maxs[0,0],300),
            np.linspace(mins[0,1], maxs[0,1], 300));

    # evaluate model on the dense grid
    Z = pred_func(np.c_[xs.flatten(), ys.flatten()]);
    Z = Z.reshape(xs.shape)
    # Plot the contour and training examples
    plt.contourf(xs, ys, Z, cmap=plt.cm.Spectral)
    x1 = np.squeeze(np.asarray(X[:,0]))
    x2 = np.squeeze(np.asarray(X[:,1]))
    y1 = Y[:,1]
    print(x1)
    print(x2)
    print(y1)
    plt.scatter(x1, x2, c=y1, s=50,cmap=colors.ListedColormap(['orange', 'blue']))
    plt.show()
