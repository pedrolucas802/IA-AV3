import numpy as np
import matplotlib.pyplot as plt

def f(x1, x2):  # domínio |-100 , 100|
    return x1**2 + x2**2

x1 = np.linspace(-100, 100, 1000)
X1, X2 = np.meshgrid(x1, x1)
Y = f(X1, X2)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X1, X2, Y, cmap='jet', alpha=0.6)


ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('f(x1, x2)')


itMax = 1000

xl = [-100,-100]
xu = [100,100]
Localsigma = 0.9
LocalXbest1 = np.random.uniform(xl[0],xu[0])
LocalXbest2 = np.random.uniform(xl[1],xu[1])
Fbest = f(LocalXbest1,LocalXbest2)
ax.scatter(LocalXbest1, LocalXbest2, Fbest, marker='x', color='purple',linewidths = 2)
i=0
while(i<itMax):
    n = np.random.normal(0,Localsigma)
    Xcand1 = LocalXbest1 + n
    Xcand2 = LocalXbest2 + n
   # Verificar a violação da restrição em caixa.
    if Xcand1 < xl[0]:
        Xcand1 = xl[0]
    if Xcand1 > xu[0]:
        Xcand1 = xu[0]
    if Xcand2 < xl[1]:
        Xcand2 = xl[1]
    if Xcand2 > xu[1]:
        Xcand2 = xu[1]
    # AcabouVerificação
    Fcand = f(Xcand1,Xcand2)
    if(Fcand < Fbest):
        LocalXbest1 = Xcand1
        LocalXbest2 = Xcand2
        Fbest = Fcand
        ax.scatter(LocalXbest1, LocalXbest2, Fbest, marker='x', color='k', alpha=0.3)
        plt.pause(0.1)
    i+=1

ax.scatter(LocalXbest1, LocalXbest2, Fbest, marker='x', color='green',linewidths = 2)
plt.show()

bp=0