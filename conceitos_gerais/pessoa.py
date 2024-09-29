class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    
    @classmethod
    def outro_construtor(cls, nome):
        return cls(nome)

p = Pessoa("Renan")
print(p.nome)

p2 = Pessoa.outro_construtor("Cristiano")
print(p2.nome)