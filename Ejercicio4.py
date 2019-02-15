class Fraccion():
    def __init__(self,fraccion1,fraccion2):
        self.fraccion1 = fraccion1
        self.fraccion2 = fraccion2

    def suma(self):
        suma = float(self.fraccion1) + float(self.fraccion2)
        return suma 

    def resta(self):
        restar = float(self.fraccion1) - float(self.fraccion2)
        return resta

    def multiplicar(self):
        multiplicar = float(self.fraccion1)*float(self.fraccion2)
        return multiplicar

    def dividir(self):
        dividir = float(self.fraccion1)/float(self.fraccion2)
        return dividir

