def maxi(*l):
    if len(l) == 0:
        return 0
    
    m = l[0]
    
    for ix in range(len(l)):
        if l[ix] > m:
            m = l[ix]

    return m

def mini(*l):
    if len(l) == 0:
        return 0
    
    m = l[0]
    
    for ix in range(len(l)):
        if l[ix] < m:
            m = l[ix]

    return m

def media(*l):
    if len(l) == 0:
        return 0
        
    suma = 0 
    for valor in l:
       suma += valor
       
    return suma / len(l)
'''
print(maxi(1, 3, -1, 15, 9))
print(mini(1, 3, -1, 15, 9))
print(media(1, 3, -1, 15, 9))
'''

funciones = {
    'max' : maxi,
    'min' : mini,
    'med' : media
    }


def returnF(nombre):
    nombre = nombre.lower()
    if nombre in funciones.keys():
        return funciones[nombre]
    
    return None