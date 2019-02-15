class Cuenta():
    def __init__(self,metodo_ingreso, reintegro,transferencia):
        self.metodo_ingreso = metodo_ingreso
        self.reintegro = reintegro
        self.transferencia = transferencia

    def get_metodo_ingreso(self):
        return self.metodo_ingreso
    
    def get_reintegro(self):
        return self.reintegro

    def get_transferencia(self):
        return self.transferencia


a = Cuenta("Ingreso bancario",200,1800)
print(a.get_metodo_transferencia(),a.get_reintegro(),a.get_transferencia())
