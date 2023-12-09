import numpy as np
import matplotlib . pyplot as plt

def f(x1 , x2 ): #dominio x1 = |-2 , 4| x2 = |-2 , 5|
    return (np.exp(-(x1**2 + x2**2)) + 2 * np.exp(-((x1-1.7)**2 + (x2-1.7)**2)))

def P(Fj , Fi):
    return np.exp(-((Fj-Fi)/T))

x1 = np.linspace(-2, 4, 1000)
X1, X2 = np.meshgrid(x1, x1)
Y = f(X1, X2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X1, X2, Y, cmap='jet', alpha=0.6)

ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('f(x1, x2)')

itMax = 1000
T=1000
xl = [-2,-2]
xu = [4,5]
TemperaSigma = 2
TemperaXbest1 = np.random.uniform(xl[0],xu[0])
TemperaXbest2 = np.random.uniform(xl[1],xu[1])
TemperaFbest = f(TemperaXbest1,TemperaXbest2)
i=0
contador = 0
while(i<itMax):
    n = np.random.normal(0,TemperaSigma)
    Xcand1 = TemperaXbest1 + n
    Xcand2 = TemperaXbest2 + n
    if Xcand1 < xl[0]:
        Xcand1 = xl[0]
    if Xcand1 > xu[0]:
        Xcand1 = xu[0]
    if Xcand2 < xl[1]:     
        Xcand2 = xl[1]
    if Xcand2 > xu[1]:
        Xcand2 = xu[1]
    Fcand = f(Xcand1,Xcand2)
    if(Fcand < TemperaFbest):
        contador =0
        TemperaXbest1 = Xcand1
        TemperaXbest2 = Xcand2
        TemperaFbest = Fcand
        ax.scatter(TemperaXbest1, TemperaXbest2, TemperaFbest, marker='x', color='k', linewidths=2)
        plt.pause(0.1)
    elif(P(Fcand,TemperaFbest)>= np.random.uniform(low=0,high=1)):
        TemperaXbest1 = Xcand1
        TemperaXbest2 = Xcand2
        TemperaFbest = Fcand
        ax.scatter(TemperaXbest1, TemperaXbest2, TemperaFbest, marker='x', color='k', linewidths=2)
        plt.pause(0.1)
    i+=1
    T = 0.99*T
        
ax.scatter(TemperaXbest1, TemperaXbest2, TemperaFbest, marker='x', color='green',s=100,linewidths=5)
plt.show()