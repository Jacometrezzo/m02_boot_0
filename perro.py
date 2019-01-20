class Perro():
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        
    def ladrar(self):
        if self.peso >= 8:
            print('GUAU GUAU')
        else:
            print('Guau, Guau')
            
    def __str__(self):
        return 'Perro {}, edad: {}, peso: {}'.format(self.nombre, self.edad, self.peso)
    
    
        
    
        
        