import os
os.system("cls")
a = []
b = []
c = []
cont_mas = 0
cont_fem = 0

import os
os.system("cls")
while True:
    n = input("Ingrese nombre:")
    m = input("Ingrese sexo:")
    k = int(input("Ingrese edad:"))
    if 4<k<18:
        a.append(n)
        b.append(m)
        c.append(k)
    if m == "masculino":
        cont_mas = cont_mas+1
    if m == "femenino":
        cont_fem = cont_fem+1
    if len(c)==5:
        break
suma_edad = 0
cant_edad = 0
for i in c :
    suma_edad = suma_edad+i
    cant_edad = cant_edad+1
prom_edad = suma_edad/cant_edad

    

print("Lista de inscritos:")
print("los nombres son",a)
print("los sexos respectivamente son:",b)
print("las edades respectivamente son",c)
print("Hay",cont_mas,"hombres")
print("Hay",cont_fem,"mujeres")
print("el promedio de las edades es:",prom_edad)
