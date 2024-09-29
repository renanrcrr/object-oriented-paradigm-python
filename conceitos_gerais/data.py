class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        print(self)
    
    @classmethod
    def de_string(cls, data_string): # 10-12-2024
        dia, mes, ano = map(int, data_string.split('-'))
        data = cls(dia, mes, ano)
        return data
    
    @staticmethod
    def is_date_valid(data_string):
        dia, mes, ano = map(int, data_string.split('-'))
        return dia <= 31 and mes <= 12 and ano <= 2020

data = Data(10, 5, 1999)
data1 = Data.de_string("29-10-2001")
print(data1)
verdade = Data.is_date_valid("10-09-2002")
print(verdade)