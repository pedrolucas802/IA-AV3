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


xl = [0,0]
xu = [np.pi,np.pi]
Localsigma = 0.9
LocalXbest1 = np.random.uniform(xl[0],xu[0])
LocalXbest2 = np.random.uniform(xl[1],xu[1])
Fbest = f(LocalXbest1,LocalXbest2)
ax.scatter(LocalXbest1, LocalXbest2, Fbest, marker='x', color='purple',linewidths = 2)
i=0
contador = 0
while(i<itMax):
    n = np.random.normal(0,Localsigma,size=(2,1))
    Xcand1 = LocalXbest1 + n[0,0]
    Xcand2 = LocalXbest2 + n[1,0]
   # Verificar a violação da restrição em caixa.
    if Xcand1 < xl[0]:
        Xcand1 = xl[0]
    if Xcand1 > xu[0]:
        Xcand1 = xu[0]
    if Xcand2 < xl[1]:      #Essa verificação deve estra errada
        Xcand2 = xl[1]
    if Xcand2 > xu[1]:
        Xcand2 = xu[1]
    # AcabouVerificação
    Fcand = f(Xcand1,Xcand2)
    if(Fcand < Fbest):
        LocalXbest1 = Xcand1
        LocalXbest2 = Xcand2
        Fbest = Fcand
        ax.scatter(LocalXbest1, LocalXbest2, Fbest, marker='x', color='k', linewidths=2)
        plt.pause(0.1)
        contador = 0
    else:
        contador += 1
    if contador == 50:
        break
    i+=1

ax.scatter(LocalXbest1, LocalXbest2, Fbest, marker='x', color='green',s=100,linewidths=5)
plt.show()

bp=4