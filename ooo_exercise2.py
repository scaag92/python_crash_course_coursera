class estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print(f'El estudiante {self.nombre} esta estudiando' )

x = input('Enter your name: ')
age = input('Enter your age: ')
gr = input('Enter your grade: ')

estudiante1 = estudiante(x,age,gr)
estudiante1.estudiar()
