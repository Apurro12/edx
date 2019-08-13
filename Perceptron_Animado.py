import random
from matplotlib import pyplot as plt
from math import sqrt,cos,sin,pi
import numpy as np
import funciones

points,x_s,y_s,c_s = funciones.circulo(500)
th = [0,0,0,0,0]


#Visualizacion de la dinamica del ecosistema
plt.axis([-1,1,-1,1])
plt.ion()

y, x = np.ogrid[-1.3:1.3:100j, -1.3:1.3:100j]
plt.scatter(x_s,y_s,c = c_s)

plt.contour(x.ravel(), 
            y.ravel(), 
            th[0]*x+th[1]*y+ th[2] + th[3]* (x**3) + th[4]* (y**4) , 
            [0], #aca van los contornos
            colors='red',)

plt.axis([-1.3, 1.3, -1.3, 1.3])
plt.axis("scaled")

plt.pause(0.2)
plt.cla()

for _ in range(100):

	random.shuffle(points)
	points_aux = points[slice(0,500,1)]

	th = funciones.Perceptron_Cuartico(1,points_aux,th)
	
	plt.scatter(x_s,y_s,c = c_s)

	plt.contour(x.ravel(), 
            y.ravel(), 
            th[0]*x+th[1]*y+ th[2] + th[3]* (x**3) + th[4]* (y**4) , 
            [0], #aca van los contornos
            colors='red',)


	plt.axis([-1.3, 1.3, -1.3, 1.3])
	plt.axis("scaled")
	plt.show()
	
#	plt.savefig(str(_)+'.png', dpi=100)
	plt.pause(0.2)
	
	plt.cla()


