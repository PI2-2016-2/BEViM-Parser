from scipy import integrate
import numpy as np

def numerical_integration(y_array, x_array):
	return integrate.cumtrapz(y_array, x_array, initial=0)

##############################################################

array_y = [0.00, 1.00, 0.00, -1.00, 0.00, 1.00, 0.00, -1.00, 0.00, 1.00]
array_x = [0.00, 25.00, 50.00, 75.00, 100.00, 125.00, 150.00, 175.00, 200.00, 225.00]

print("Array de y...\n")
print(array_y)

print("Array de x...\n")
print(array_x)

print("Tamanho do x...\n")
print(len(array_x))

print("Tamanho do y...\n")
print(len(array_y))

returned_array_one = numerical_integration(array_y, array_x)

print("Array retornado pelo método de integração (Chamada 1)...\n")
print(returned_array_one)

print("Tamanho do array retornado pelo método (Chamada 1)...\n")
print(len(returned_array_one))

returned_array_two = numerical_integration(returned_array_one, array_x)
 
print("Array retornado pelo método de integração (Chamada 2)...\n");
print(returned_array_two)

print("Tamanho do array retornado pelo método (Chamada 2)...\n")
print(len(returned_array_two))
