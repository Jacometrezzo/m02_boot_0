from functools import reduce

def doble(x):
    return x + x


lista = [1, 3, -1, 15, 9]
l = [1, 2, 3, 8, 9, 16]

listaDobles = map(lambda x: x*2, lista)

listaPares = filter(lambda x: x % 2 == 0, l)

listaDobles1 = map(doble, lista)

def esPar(x):
    return x % 2 == 0

listaPares1 = filter(esPar, l)

sumatorio = reduce(lambda x, y: x + y, lista)
suma100 = reduce(lambda x,y: x+y, range(101))

print(list(listaDobles))
print(list(listaPares))
print(list(listaDobles1))
print(list(listaPares1))
print(sumatorio)
print(suma100)

print(sumatorio ,'\n', suma100)

 
