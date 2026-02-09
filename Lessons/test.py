
class Personaje():
    def __init__(self,nombre,fuerza,velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad

    def __repr__ (self):
        return f"Nommbre: {self.nombre}     Fuerza:{self.fuerza}    Velocidad:{self.velocidad}"

    def __add__(self,nuevo_objeto):
        nuevo_nombre = self.nombre + "-" + nuevo_objeto.nombre
        nuevo_fuerza = round(((self.fuerza + nuevo_objeto.fuerza)/2)**2)
        nuevo_velocidad = round(((self.velocidad + nuevo_objeto.velocidad)/2)**2)
        return Personaje(nuevo_nombre, nuevo_fuerza, nuevo_velocidad)

goku = Personaje("Goku",100,100)
vegeta = Personaje("Vegeta",80,80)
gogueta = goku + vegeta

print(gogueta)
