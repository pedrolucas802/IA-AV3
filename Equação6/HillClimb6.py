import statistics
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

moda_x1 = []
moda_x2 = []
moda_f = []

p = 0
while p < 100:
    itMax = 1000

    xl = [-5.12,-5.12]
    xu = [5.12,5.12]
    X0_1 = 1
    X0_2 = 1
    E = 0.8
    maxNeighbor = 20
    Hill_Xbest1 = X0_1
    Hill_Xbest2 = X0_2
    Hill_Fbest = f(Hill_Xbest1, Hill_Xbest2)
    k = 0
    melhoria = True
    contador = 0
    while k < itMax and melhoria:
        l = 0
        melhoria = False
        while l < maxNeighbor:
            l += 1
            y1 = np.random.uniform(low=Hill_Xbest1 - E, high=Hill_Xbest1 + E)
            y2 = np.random.uniform(low=Hill_Xbest2 - E, high=Hill_Xbest2 + E)
            
            if y1 < xl[0]:
                y1 = xl[0]
            if y1 > xu[0]:
                y1 = xu[0]
            if y2 < xl[1]:      #Essa verificação deve estra errada
                y2 = xl[1]
            if y2> xu[1]:
                y2 = xu[1]
            F = f(y1, y2)   
            if F > Hill_Fbest:
                contador= 0
                Hill_Xbest1 = y1
                Hill_Xbest2 = y2
                Hill_Fbest = F
                melhoria = True
                break
            else:
                contador += 1
            if contador == 50:
                break
        k += 1
    moda_x1.append(Hill_Xbest1)
    moda_x2.append(Hill_Xbest2)
    moda_f.append(Hill_Fbest)

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