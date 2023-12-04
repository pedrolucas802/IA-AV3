import numpy as np
import matplotlib . pyplot as plt

def f(x1 , x2 ): #dominio |-8 , 8|
    return (-20 * np.exp(-0.2 * np.sqrt(0.5 * (x1**2 + x2**2))) - np.exp(0.5 * (np.cos(2 * x1 * np.pi) + np.cos(2 * x2 * np.pi))) + 20 + np.exp(1))

x1 = np.linspace ( -8 ,8 ,1000)
X1 , X2 = np . meshgrid (x1 , x1 )
Y = f(X1 , X2 )


fig = plt.figure ()
ax = fig.add_subplot ( projection ='3d')
ax.plot_surface ( X1 ,X2 ,Y , rstride =10 , cstride =10 , alpha =0.6 , cmap ='jet')


ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('f(x1, x2)')


itMax = 1000

# HILL CLIMBING------------------------------------------------------------------------
X0_1 = -8
X0_2 = 8
E = 5
maxNeighbor = 30
Hill_Xbest1 = X0_1
Hill_Xbest2 = X0_2
Hill_Fbest = f(Hill_Xbest1, Hill_Xbest2)
k = 0
melhoria = True
ax.scatter(Hill_Xbest1, Hill_Xbest2, Hill_Fbest, marker='x', color='purple',linewidths = 2)
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
            ax.scatter(y1, y2, F, marker='x', color='k', alpha=0.3)
            plt.pause(0.1)
            break
    k += 1


ax.scatter(Hill_Xbest1, Hill_Xbest2, Hill_Fbest, marker='x', color='green')

plt.show()




bp=2