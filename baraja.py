import random
palos =['o', 'c', 'e', 'b']
numeros =['A', '2', '3', '4', '5', '6', '7', 'S', 'C', 'R']

def crearBaraja():
    baraja = []
    for numero in numeros:
        for palo in palos:
            baraja.append(numero+palo)
    return(baraja)

def intercambio(a, b):
    aux = a
    a = b
    b = aux
    return a, b
def barajar(lista):
    for i in range(len(lista)):
        nueva_poz = random.randrange(len(lista))
        #intercambio(lista[i], lista[nueva_poz])
        aux = lista[i]
        lista[i] = lista[nueva_poz]
        lista[nueva_poz] = aux
    return lista
if __name__ == "__main__":
    print(crearBaraja())
    print(barajar(crearBaraja()))
