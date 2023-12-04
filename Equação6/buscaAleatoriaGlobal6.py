import numpy as np
import matplotlib . pyplot as plt

def f(x1 , x2 ):
    return (x1 * np.sin(4 * np.pi * x1) - x2 * np.sin(4 * np.pi * x2 + np.pi) + 1)

x1 = np.linspace ( -1 ,3 ,1000)
X1, X2 = np.meshgrid(x1, x1)
Y = f(X1, X2)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X1, X2, Y, cmap='jet', alpha=0.6)


ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('f(x1, x2)')


itMax = 1000

xl = [-1,-1]
xu = [3,3]
GlobalXbest1 = np.random.uniform(xl[0],xu[0])
GlobalXbest2 = np.random.uniform(xl[1],xu[1])
GlobalFbest = f(GlobalXbest1,GlobalXbest2)
ax.scatter(GlobalXbest1, GlobalXbest2, GlobalFbest, marker='x', color='purple',linewidths = 3)
j=0
contador = 0
while(j<itMax):
    GlobalXcand1 = np.random.uniform(xl[0],xu[0])
    GlobalXcand2 = np.random.uniform(xl[1],xu[1])
    GlobalFcand = f(GlobalXcand1,GlobalXcand2)
    if(GlobalFcand > GlobalFbest):
        contador = 0
        GlobalXbest1 = GlobalXcand1
        GlobalXbest2 = GlobalXcand2
        GlobalFbest = GlobalFcand
        ax.scatter(GlobalXbest1, GlobalXbest2, GlobalFbest, marker='x', color='k',linewidths=2 )
        plt.pause(0.1)
    else:
        contador += 1
    if contador == 50:
        break
    j+=1

ax.scatter(GlobalXbest1, GlobalXbest2, GlobalFbest, marker='x', color='green',s=100,linewidths = 5)
plt.show()