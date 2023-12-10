import statistics
import numpy as np
import matplotlib . pyplot as plt

def f(x1 , x2 ):
    return ((x1**2 - 10 * np.cos(2 * x1 * np.pi) + 10) + (x2**2 -10 * np.cos(2 * np.pi * x2) + 10))

x1 = np.linspace ( -5.12 ,5.12 ,1000)

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


    xl = [-5.12,-5.12]
    xu = [5.12,5.12]
    Localsigma = 1.5
    LocalXbest1 = np.random.uniform(xl[0],xu[0])
    LocalXbest2 = np.random.uniform(xl[1],xu[1])
    Fbest = f(LocalXbest1,LocalXbest2)
    i=0
    contador = 0
    while(i<itMax):
        n = np.random.normal(0,Localsigma)
        Xcand1 = LocalXbest1 + n
        Xcand2 = LocalXbest2 + n
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
            contador = 0
            LocalXbest1 = Xcand1
            LocalXbest2 = Xcand2
            Fbest = Fcand
        else:
            contador += 1
        if contador == 50:
            break
        i+=1
    moda_x1.append(LocalXbest1)
    moda_x2.append(LocalXbest2)
    moda_f.append(Fbest)
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