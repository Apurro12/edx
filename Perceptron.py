import random
from matplotlib import pyplot as plt
from math import sqrt,cos,sin,pi
import numpy as np
import funciones

points,x_s,y_s,c_s = funciones.circulo(500)
th = funciones.Perceptron_Cuartico(200,points)
print(th)



#Aca grafico directamente teniendo en cuenta el contorno
y, x = np.ogrid[-1.3:1.3:100j, -1.3:1.3:100j]
plt.scatter(x_s,y_s,c = c_s)
plt.contour(x.ravel(), 
            y.ravel(), 
            th[0]*x+th[1]*y+th[2]* (x**2 + y**2) + th[3] , 
            [0], #aca van los contornos
            colors='red',)
plt.axis([-1.3, 1.3, -1.3, 1.3])
plt.axis("scaled")
plt.show()
