import random
from matplotlib import pyplot as plt
from math import sqrt,cos,sin,pi
import numpy as np
import funciones

points,x_s,y_s,c_s = funciones.parabola(500)
th = funciones.Perceptron_Parabolico(50,points)
print(th)
print([- (th[0] / th[1] ) , - (th[2] / th[1]) ])


x_sep = [0.1*j for j in range(-10,11)]
y_sep = [- (th[0] / th[1] ) * x - (th[2] / th[1] ) * (x**2)  for x in x_sep]
#Con estos dos grafico una linea
#y_sep =  [- (th[0] / th[1] ) * x for x in x_sep]




plt.scatter(x_s,y_s,c = c_s)
plt.plot(x_sep,y_sep,c ="g")
#plt.axis("equal")
plt.axis([-1.1, 1.1, -1.1, 1.1])
plt.show()