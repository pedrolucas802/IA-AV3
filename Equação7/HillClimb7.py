import numpy as np
import matplotlib . pyplot as plt

def f(x1 , x2 ):
    return (-np.sin(x1) * np.sin((x1**2)/np.pi)**20 - np.sin(x2) * np.sin((2 * x2**2)/np.pi)**20)

x1 = np.linspace ( 0 , np.pi ,1000)

X1, X2 = np.meshgrid(x1, x1)
Y = f(X1, X2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X1, X2, Y, cmap='jet', alpha=0.6)

ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('f(x1, x2)')


itMax = 1000

# HILL CLIMBING--------------------------------------------------------NÃO ESTÁ CONSTANTE----------------
X0_1 = np.pi
X0_2 = 0
E = 0.5
maxNeighbor = 20
Hill_Xbest1 = X0_1
Hill_Xbest2 = X0_2
Hill_Fbest = f(Hill_Xbest1, Hill_Xbest2)
k = 0
melhoria = True
ax.scatter(Hill_Xbest1, Hill_Xbest2, Hill_Fbest, marker='x', color='purple',linewidths=3)
contador = 0
while k < itMax and melhoria:
    l = 0
    melhoria = False
    while l < maxNeighbor:
        l += 1
        y1 = np.random.uniform(low=Hill_Xbest1 - E, high=Hill_Xbest1 + E)
        y2 = np.random.uniform(low=Hill_Xbest2 - E, high=Hill_Xbest2 + E)
        F = f(y1, y2)
        
        if F < Hill_Fbest:
            contador = 0
            Hill_Xbest1 = y1
            Hill_Xbest2 = y2
            Hill_Fbest = F
            melhoria = True
            ax.scatter(y1, y2, F, marker='x', color='k', linewidths=2)
            plt.pause(0.1)
            break
        
    if contador == 50:
        break
    k += 1
    contador += 1
    


ax.scatter(Hill_Xbest1, Hill_Xbest2, Hill_Fbest, marker='x', color='green',s=100,linewidths=5)

plt.show()