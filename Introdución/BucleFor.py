#Codigo para usar un bucle for

a=[7,3,6,5]
b=1

"""
Un for con range(int) se repetira tantas veces como el valor del int 
en cada iteración ira tomando valores desde 0 hasta int
"""
for i in range(4):
    print(i,"->",a[i])

print("fin bucle",b)
b+=1
#el int tambien puede ser una variable
for i in range(b):
    print(i,"->",a[i])

print("fin bucle",b)
b+=1
"""
Un for que recorre una lista se repetira tatnas vces como elementos en la lista
en cada iteración tomara un valor de la lista por orden
"""
for i in a: 
    print(i)
 
print("fin bucle",b)
b+=1
#La lista no tien porque estar inicializada
for i in [3,5,6]:
    print("i vale ",i)
    
print("fin bucle",b)
b+=1    

#Pero no solo funciona con listas
for i in "BUCLE":
    print(i)
    
print("fin del BUCLE")