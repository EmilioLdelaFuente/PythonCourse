#Este codigo es para aprender a usar los condicionales 'if' e 'if else'

print("Escribe un numero")
a=int(input())
print("Escribe otro numero")
b=int(input()) 
#el condicional if funciona como en cualquier otro lenguaje
if a>b: 
    print("El primer numero es mayor") #si se cumple la condicion entra
elif a<b: #si no pasa a la siguiente condicion
    print ("El segundo numero es mayor")
else:
    print ("Son iguales...")