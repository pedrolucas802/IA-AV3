import statistics
import numpy as np
import matplotlib . pyplot as plt

def f(x1 , x2 ): #dominio |-8 , 8|
    return (-20 * np.exp(-0.2 * np.sqrt(0.5 * (x1**2 + x2**2))) - np.exp(0.5 * (np.cos(2 * x1 * np.pi) + np.cos(2 * x2 * np.pi))) + 20 + np.exp(1))

def P(Fj , Fi):
    return np.exp(-((Fj-Fi)/T))

x1 = np.linspace ( -8 ,8 ,1000)

X1, X2 = np.meshgrid(x1, x1)
Y = f(X1, X2)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X1, X2, Y, cmap='jet', alpha=0.6)


ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('f(x1, x2)')

moda_x1 = []
moda_x2 = []
moda_f = []

p = 0
while p < 100:
    itMax = 1000
    T=1000

    xl = [-8,-8]
    xu = [8,8]
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
        elif(P(Fcand,TemperaFbest)>= np.random.uniform(low=0,high=1)):
            TemperaXbest1 = Xcand1
            TemperaXbest2 = Xcand2
            TemperaFbest = Fcand
        i+=1
        T = 0.99*T
    moda_x1.append(TemperaXbest1)
    moda_x2.append(TemperaXbest2)
    moda_f.append(TemperaFbest)
    p+=1
        
# Calcula a moda
moda_x1 = np.array(moda_x1)
moda_x2 = np.array(moda_x2)
moda_f = np.array(moda_f)

moda_x1_final = statistics.mode(moda_x1)
moda_x2_final = statistics.mode(moda_x2)
moda_f_final = statistics.mode(moda_f)

# Plota a moda no gráfico
ax.scatter(moda_x1_final, moda_x2_final, moda_f_final, marker='x', color='green', s=100, linewidths=5)
plt.show()
