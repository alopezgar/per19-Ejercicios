class Empleado():
     def __init__(self,nombre,sueldo,impuestos):
         self.nombre = nombre
         self.sueldo = sueldo
         self.impuestos = impuestos

     def get_nombre(self):
         return self.nombre

     def get_sueldo(self):
         return self.sueldo

     def get_impuestos(self):
         return self.impuestos

empleado1 = Empleado ("Javier",1800,200)
print(empleado1.get_nombre(), empleado1.get_sueldo(),empleado1.get_impuestos())
