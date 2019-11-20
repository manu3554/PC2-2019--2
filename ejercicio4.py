import random
while True:
    n = int(input("Ingrese el tamaño de la matriz:"))
    if 1<n<6:
        break 
a =[]
can_pares=0
for i in range(n):
    b = random.randint(1,101)
    a.append(b)
    print(b)
    if b % 2 == 0:
        can_pares = can_pares+1
print("el arreglo es",a)
print("la cantidad de pares es:",can_pares)

