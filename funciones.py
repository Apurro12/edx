import random
from math import cos,sin,pi
import numpy as np

#Datasets que distribuyen puntos

#Separacion lineal en el cuadrado de lado 1
def datos(cantidad):
	angulo = random.random()*2*pi
	points = []
	for j in range(cantidad):
	    aux = [random.random()*2-1,random.random()*2-1]
	    if (aux[0]*cos(angulo) + aux[1]*sin(angulo) > 0 ):
	      aux.append(1)
	    else:
	      aux.append(-1)
	    points.append(aux)
	    
	x_s = [item[0] for item in points]
	y_s = [item[1] for item in points]
	c_s = ["r" if item[2] > 0 else "b" for item in points]

	return((points,x_s,y_s,c_s))



def parabola(cantidad):
	"""Los puntos son ternas x,y,label"""
	points = []
	for j in range(cantidad):
	    aux = [random.random()*2-1,random.random()*2-1]
	    if (10*( aux[0]**2 ) + 4* aux[0] > aux[1] ):
	      aux.append(1)
	    else:
	      aux.append(-1)
	    points.append(aux)
	    
	x_s = [item[0] for item in points]
	y_s = [item[1] for item in points]
	c_s = ["r" if item[2] > 0 else "b" for item in points]

	return((points,x_s,y_s,c_s))




def Perceptron_Lineal(epochs,points):
	th = [0,0]
	for _ in range(epochs):
	    for j in range(len(points)):
	        if  ( dot( th, points[j]  ) * points[j][2] <= 0 ):
	            producto = [points[j][2] * points[j][p] for p in range(2)]
	            th = suma_vec(th,producto)

	return(th)		


def Perceptron_Parabolico(epochs,points):
	th = [0,0,0]
	for _ in range(epochs):
	    for j in range(len(points)):
	        if  ( dot( th, ampliar(points[j])  ) * points[j][2] <= 0 ):
	            producto = [points[j][2] * ampliar(points[j])[p] for p in range(3) ]
	            th = suma_vec(th,producto)

	return(th)		


def ampliar(vec):
	vec_aux = vec[:]
	label = vec_aux.pop()
	vec_aux.append(vec[0]**2)
	vec_aux.append(label)
	return vec_aux



dot  = lambda x,y: sum(i[0]*i[1] for i in zip(x,y))
suma_vec = lambda th,producto: [i[0] + i[1] for i in zip(th,producto) ]