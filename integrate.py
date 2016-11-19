from scipy import integrate
import numpy as np

def numerical_integration(y_array, x_array):
	return integrate.cumtrapz(y_array, x_array, initial=0)

##############################################################

array_x = np.linspace(-2, 10, num=250)
array_y = array_x

print("Array de y...\n")
print(array_y)

print("Array de x...\n")
print(array_x)
print("Tamanho do X...\n")
print(len(array_x))

returned_array = numerical_integration(array_y, array_x)

print("Array retornado pelo método de integração...\n")
print(returned_array)

print("Tamanho do array retornado pelo método...\n")
print(len(returned_array))
