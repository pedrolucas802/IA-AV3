import numpy as np
import matplotlib . pyplot as plt

def f(x1 , x2 ):
    return (-(x2 + 47) * np.sin(np.sqrt(np.abs(x1/2 + (x2 + 47)))) - x1 * np.sin(np.sqrt(np.abs(x1 - (x2 + 47)))))

x1 = np.linspace ( -200 ,20 ,1000)

X1, X2 = np.meshgrid(x1, x1)
Y = f(X1, X2)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X1, X2, Y, cmap='jet', alpha=0.6)


ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('f(x1, x2)')


itMax = 1000

xl = [-200,-200]
xu = [20,20]
GlobalXbest1 = np.random.uniform(xl[0],xu[0])
GlobalXbest2 = np.random.uniform(xl[1],xu[1])
GlobalFbest = f(GlobalXbest1,GlobalXbest2)
ax.scatter(GlobalXbest1, GlobalXbest2, GlobalFbest, marker='x', color='purple',linewidths = 3)
contador = 0
j=0
while(j<itMax):
    GlobalXcand1 = np.random.uniform(xl[0],xu[0])
    GlobalXcand2 = np.random.uniform(xl[1],xu[1])
    GlobalFcand = f(GlobalXcand1,GlobalXcand2)
    if(GlobalFcand < GlobalFbest):
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