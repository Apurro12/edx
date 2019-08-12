import random
from matplotlib import pyplot as plt
from math import sqrt,cos,sin,pi
import numpy as np
import funciones

points,x_s,y_s,c_s = funciones.potencia_cuarta(500)
th = [0,0,0,0]


#Visualizacion de la dinamica del ecosistema
plt.axis([-1,1,-1,1])
plt.ion()


x_sep = [0.05*j for j in range(-20,21)]
y_sep = [0  for x in x_sep]

plt.axis([-1.1, 1.1, -1.1, 1.1])
plt.scatter(x_s,y_s,c = c_s)
plt.plot(x_sep,y_sep,c ="g")

plt.savefig(str(-1)+'.png', dpi=100)
plt.pause(0.2)
	
plt.cla()



for _ in range(100):

	random.shuffle(points)
	points_aux = points[slice(0,500,1)]

	th = funciones.Perceptron_Cuartico(20,points_aux,th)
	
	x_sep = [0.05*j for j in range(-20,21)]
	y_sep = [- (th[0] / th[1] ) * x - (th[2] / th[1] ) * (x**2) - (th[3] / th[1] ) * (x**4)  for x in x_sep]

	plt.axis([-1.1, 1.1, -1.1, 1.1])
	plt.scatter(x_s,y_s,c = c_s)
	plt.plot(x_sep,y_sep,c ="g")
	
#	plt.savefig(str(_)+'.png', dpi=100)
	plt.pause(0.2)
	
	plt.cla()


