class Fecha():
    def __init__(self,dia,mes,año):
        self.dia = dia
        self.mes = mes
        self.año = año

    def get_dia(self):
        return self.dia

    def get_mes(self):
        return self.mes

    def get_año(self):
        return self.año

    def comprobar_fecha(self):
        if (0 < int(dia) <= 31) and (1 <= int(mes) <= 12) and año.isdigit():
            print("La fecha introducida es correcta.")
        else:
            print("La fecha introducida es incorrecta.")

    def nueva_fecha(self):
        dia = dia + 1
        return self.dia
