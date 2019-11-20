import random
while True:
    n = int(input("Ingrese el tamaño de la matriz:"))
    if 1<n<6:
        break 
a =[]
x = []
c = []
d =[]
e = []
can_pares=0
for i in range(n):
    if n==2:

        b = random.randint(1,101)
        a.append(b)
        x.append(b)

        
        if b % 2 == 0:
            can_pares = can_pares+1
    if n == 3:
        b = random.randint(1,101)
        a.append(b)
        x.append(b)
        c.append(b)
        if b % 2 == 0:
            can_pares = can_pares+1
    if n == 4:
        b = random.randint(1,101)
        a.append(b)
        x.append(b)
        c.append(b)
        d.append(b)
        if b % 2 == 0:
            can_pares = can_pares+1
    
    if n == 5:
        b = random.randint(1,101)
        a.append(b)
        x.append(b)
        c.append(b)
        d.append(b)
        e.append(b)
        if b % 2 == 0:
            can_pares = can_pares+1
    

print(a)
print(x)
print(c)
print(d)
print(e)

print("la cantidad de pares es:",can_pares)

