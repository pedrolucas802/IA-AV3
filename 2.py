import numpy as np
import matplotlib . pyplot as plt

def f(x1 , x2 ): #dominio x1 = |-2 , 4| x2 = |-2 , 5|
    return (np.exp(-(x1**2 + x2**2)) + 2 * np.exp(-(x1-1.7)**2 + (x2-1.7)**2))

x1 = np.linspace ( -2 ,4 ,1000)
x2 = np.linspace(-2,5,1000)
X1 , X2 = np.meshgrid (x1 , x2 )
Y = f(X1 , X2 )




fig = plt.figure ()
ax = fig.add_subplot ( projection ='3d')
ax.plot_surface ( X1 ,X2 ,Y , rstride =10 , cstride =10 , alpha =0.6 , cmap ='jet')


ax.set_xlabel ('x')
ax.set_ylabel ('y')
ax.set_zlabel ('z')
ax.set_title ('f(x1 ,x2)')
plt.tight_layout ()
plt.show ()
bp=1