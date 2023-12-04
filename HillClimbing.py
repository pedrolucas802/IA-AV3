import numpy as np
import matplotlib . pyplot as plt


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


def HillClibing(itMax, X1Candidado, X2Candidado, f):
    E = 2
    maxNeighbor = 10
    Hill_Xbest1 = X1Candidado
    Hill_Xbest2 = X2Candidado
    Hill_Fbest = f
    k = 0
    melhoria = True

    while k < itMax and melhoria:
        l = 0
        melhoria = False
        while l < maxNeighbor:
            l += 1
            y1 = np.random.uniform(low=Hill_Xbest1 - E, high=Hill_Xbest1 + E)
            y2 = np.random.uniform(low=Hill_Xbest2 - E, high=Hill_Xbest2 + E)
            F = f(y1, y2)
        
            if F < Hill_Fbest:
                Hill_Xbest1 = y1
                Hill_Xbest2 = y2
                Hill_Fbest = F
                melhoria = True
                ax.scatter(y1, y2, F, marker='x', color='red', alpha=0.3)
                plt.pause(0.1)
                break
        k += 1
    return Hill_Xbest1, Hill_Xbest2, Hill_Fbest


        