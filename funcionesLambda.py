from funciones1nivel import sumaTodos

doble = lambda x: x*2

triple = lambda x : x*3

'''
print(sumaTodos(3, lambda x: x**3))
print(sumaTodos(100, lambda x :x*3))
'''

print(sumaTodos(3, doble))
print(sumaTodos(100, triple))


 