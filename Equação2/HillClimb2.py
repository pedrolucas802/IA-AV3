import statistics
import numpy as np
import matplotlib . pyplot as plt

def f(x1 , x2 ): #dominio x1 = |-2 , 4| x2 = |-2 , 5|
    return (np.exp(-(x1**2 + x2**2)) + 2 * np.exp(-((x1-1.7)**2 + (x2-1.7)**2)))

x1 = np.linspace(-2, 4, 1000)
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
    X0_1 = 4
    X0_2 = -2
    E = 0.5
    maxNeighbor = 10
    Hill_Xbest1 = X0_1
    Hill_Xbest2 = X0_2
    Hill_Fbest = f(Hill_Xbest1, Hill_Xbest2)
    k = 0
    melhoria = True
    contador =0
    while k < itMax and melhoria:
        l = 0
        melhoria = False
        while l < maxNeighbor:
            l += 1
            y1 = np.random.uniform(low=Hill_Xbest1 - E, high=Hill_Xbest1 + E)
            y2 = np.random.uniform(low=Hill_Xbest2 - E, high=Hill_Xbest2 + E)
            F = f(y1, y2)
            
            if F > Hill_Fbest:
                contador = 0
                Hill_Xbest1 = y1
                Hill_Xbest2 = y2
                Hill_Fbest = F
                melhoria = True
                break
            else:       #TALVEZ ISSO ESTÁ NO CANTO ERRADO 
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