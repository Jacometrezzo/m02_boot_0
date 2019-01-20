from functools import reduce

def sumatorioClasico(l):
    resultado = 0
    for valor in l:
        resultado += valor
        
    return resultado

def sumatorioDobleClasico (l):
    resultado = 0
    for valor in l:
        resultado += valor*2
        
    return resultado

def productoTotal(l):
    resultado = 1
    for valor in l:
        resultado *= valor
        
    return resultado
'''
#Para que funcionen las funciones de arriba
l = (1,2,3,4)

print(sumatorioClasico(l))
print(sumatorioDobleClasico(l))
print(productoTotal(l))
'''
#Explicación del problema de Reduce sumatorioDoble

lista = [1, 3, -1, 15, 9]

sumatorio = reduce(lambda x, y: x + y, lista)
#Creo una copia de la lista
l = lista[:]
#Añado el neutro para la suma de la posicion cero
l.insert(0,0)
sumatorioDobles = reduce(lambda x, y: x + y*2,l)

print(sumatorio)
print(sumatorioDobles)

