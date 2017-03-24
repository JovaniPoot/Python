print ("--intervalod de n numeros entre 20 y 60--")
print ("-----------------------------------------")
print (" ")

num=int(input("ingrese el total de numeros a usar en el intervalo"))

def generar(num):	
	lista=[]
	if num>39 :
		num2=int(input("ingrese un total que sea menor a 40 numeros"))
		generar(num2)
	else:
		for i in range(20,(20+num)):
			lista.append(i)
			print (lista)

generar(num)
