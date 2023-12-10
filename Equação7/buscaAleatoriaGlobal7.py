import statistics
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

moda_x1 = []
moda_x2 = []
moda_f = []

p = 0
while p < 100:
    itMax = 1000

    xl = [0,0]
    xu = [np.pi,np.pi]
    GlobalXbest1 = np.random.uniform(xl[0],xu[0])
    GlobalXbest2 = np.random.uniform(xl[1],xu[1])
    GlobalFbest = f(GlobalXbest1,GlobalXbest2)
    j=0
    contador = 0
    while(j<itMax):
        GlobalXcand1 = np.random.uniform(xl[0],xu[0])
        GlobalXcand2 = np.random.uniform(xl[1],xu[1])
        GlobalFcand = f(GlobalXcand1,GlobalXcand2)
        if(GlobalFcand < GlobalFbest):
            contador =0
            GlobalXbest1 = GlobalXcand1
            GlobalXbest2 = GlobalXcand2
            GlobalFbest = GlobalFcand
        else:
            contador += 1
        if contador == 50:
            break
        j+=1
    moda_x1.append(GlobalXbest1)
    moda_x2.append(GlobalXbest2)
    moda_f.append(GlobalFbest)
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