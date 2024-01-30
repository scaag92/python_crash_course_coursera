class Celular:
    def __init__(self,marca,modelo,camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    
    def llamar(self):
        print(f'Estas haciendo una llamada desde un: {self.modelo}')

    def colgar(self):
        print(f'Cortaste la llamada desde un: {self.modelo}')


celular1 = Celular("Samsung","S50","50MP")
celular2 = Celular("Iphone","15Pro","100MP",)

print(celular1.marca)

celular1.llamar()
