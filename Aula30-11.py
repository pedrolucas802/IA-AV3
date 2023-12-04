import numpy as np
import matplotlib.pyplot as plt

def torneio(P,Apt, Nt):
    S = np.empty((0,P.shape[1]))
    while(S.shape[0]!=P.shape[0]):
        sel = np.random.uniform(0,P.shape[0],size=(Nt)).astype(int)
        combatente = P[sel,:]
        apt_combatentes = Apt[sel]
        combate = np.argmin(apt_combatentes)
        vitorioso = combatente[combate,:].reshape(1,P.shape[1])
        S = np.concatenate((S,vitorioso))
        
    return S
        


def decodificador(v,lb,ub):
    s=0
    for i in range (len(v)):
        s+= v[len(v)-i-1]*2**i
    
    return lb+((ub-lb)/(2**len(v)-1))*s 

def f(x):
    return (-20*np.exp(-.2*np.abs(x)) - np.exp(np.cos(2 * x * np.pi)) + 20 + np.exp(1))

ub,lb = 5,-5
x_axis = np.linspace(lb,ub,1000)

#INICIO
P = np.random.uniform(low=0,high=2,size=(20,20)).astype(int)
Preal = np.array([decodificador(P[l,:],lb,ub) for l in range(P.shape[0])])

Apt = f(Preal)

torneio(P,Apt,2)

plt.scatter(Preal, Apt, color="k",marker="1")
    






plt.plot(x_axis,f(x_axis))
plt.show()
bp=0