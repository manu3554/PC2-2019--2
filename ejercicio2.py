def contarletra(texto,letra):
contador = 0
    for letra in texto:
        contador = contador +1
return contador

n = input("Ingrese una palabra")
contarletra(n,letra)