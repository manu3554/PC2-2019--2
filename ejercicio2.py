def contarletra(texto,letra):
    contador = 0
    for i in texto:
        if i == letra:
            contador = contador +1
    print(contador) 

n = input("Ingrese una palabra:")
m = input("letra que desea buscar:")
contarletra(n,m)

