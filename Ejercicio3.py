class Libro():
    def __init__(self,prestamo,devolucion):
        self.prestamo = prestamo
        self.devolucion = devolucion
     
    def get_prestamo(self):
        return self.prestamo

    def get_devolucion(self):
        return self.devolucion

    def get_info(self):
        return [self.prestamo, self.devolucion]


a = Libro("21 enero","3 febrero")
print(a.get_info())
