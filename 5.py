import numpy as np
import matplotlib . pyplot as plt

def f(x1 , x2 ):
    return ((x1 - 1)**2 + 100*(x2 - x1**2)**2)

x1 = np . linspace ( -100 ,100 ,1000) #Tem que ajeitar isso
X1 , X2 = np . meshgrid (x1 , x1 )
Y = f(X1 , X2 )


x1_cand , x2_cand =50 ,50
f_cand = f( x1_cand , x2_cand )

fig = plt.figure ()
ax = fig.add_subplot ( projection ='3d')
ax.plot_surface ( X1 ,X2 ,Y , rstride =10 , cstride =10 , alpha =0.6 , cmap ='jet')
ax.scatter ( x1_cand , x2_cand , f_cand , marker ='x',s =90 , linewidth =3 , color ='red')

ax.set_xlabel ('x')
ax.set_ylabel ('y')
ax.set_zlabel ('z')
ax.set_title ('f(x1 ,x2)')
plt.tight_layout ()
plt.show ()
bp=1