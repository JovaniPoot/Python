import math
print ("programa que calcula hipotenusa tomando el valor de los catetos en tipo double---")
print ("------------------------------------------------------------------------")
print (" ")

catA = float(input("igrese el valor del cateto A"))
catB = float(input("ingrese el valor del catebo B"))

def calcularHipotenusa(catA,catB):
	hipotenusa=(catA**2)+(catB**2)
	hipotenusa=math.sqrt(hipotenusa)
	hipotenusa=float(hipotenusa)
	print ("la hipotenusa es: " , hipotenusa)

calcularHipotenusa(catA,catB)
