import numpy as np
import matplotlib . pyplot as plt

def f(x1 , x2 ): # dominio  |-2,2| |-1,3|
    return ((x1 - 1)**2 + 100*(x2 - x1**2)**2)

x1 = np.linspace(-2, 2, 1000)
x2 = np.linspace(-1, 3, 1000)
X1, X2 = np.meshgrid(x1, x2)
Y = f(X1, X2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X1, X2, Y, cmap='jet', alpha=0.6)

ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('f(x1, x2)')
plt.show ()
bp=1