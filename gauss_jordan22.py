import numpy as np
import math

matriz=np.array([[5.0, 4.0, 7.0], [6.0, 8.0, 1.0]])
print "La matriz inicial es", matriz
def gaus_jordan(mat):
	pivote=mat[0,0] 
	n_filas=mat.shape[0]
	n_columnas=mat.shape[1]
	for j in range(n_columnas): #Vuelve la posicion 0,0 en un pivote de valor 1.0
		mat[0,j]=mat[0,j]/pivote
	#Sumar la fila de abajo mas la de arriba por el numero debajo del pivote para volverlo 0
	for i in range(1, n_filas):
		for j in range(i-n_columnas, n_columnas): 
			mat[i,j]=mat[i,j]-(mat[i,0]*mat[0,j])

	#Sacar el otro pivote
	for i in range(1, n_filas):
		for j in range(i-n_filas,n_columnas):
			mat[i,j]=mat[i,j]/mat[i,i]
	
	#Volver los numeros por encima de la diagonal 0
	for j in range(-1, n_columnas):
		mat[0,j]=mat[0,j]-mat[0,1]*mat[1,j]

	print "La matriz reducida es", mat	
	print "x1 =",mat[0,2],",","x2 =",mat[1,2]

	
gaus_jordan(matriz)
