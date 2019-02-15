class Rectangulo():

    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def get_perimetro(self):
        perimetro = self.base*2 + self.altura*2
        return perimetro

    def get_area(self):
        area = self.base*self.altura/2
        return area

class Prueba_rectangulo(unittest.TestCase):

    def test_rectangulo(self):
        
        rectangulo1 = Rectangulo(2,3)
        rectangulo2 = Rectangulo(1,2)

        self.assertEqual(rectangulo1.perimetro,10)
        self.assertEqual(rectangulo2.perimetro,6)
        self.assertEqual(rectangulo1.area,3)
        self.assertEqual(rectangulo2.area,1.5)

        print("El rectangulo 1 tiene perimetro",rectangulo1.perimetro, "y area",rectangulo1.area)
        print("El rectangulo 2 tiene perimetro",rectangulo2.perimetro, "y area",rectangulo2.area)
