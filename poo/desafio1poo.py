class Bicicleta:
    def __init__(self, cor, modelo, ano, valor): #construtor
        #self é igual ao this
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("plim plim...")

    def parar(self):
        print("parando a bicicleta...")
        print("bicicleta parada!")

    def correr(self):
        print("vrummmmm...")

#    def __str__(self):
#        return f"Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"

#O de baixo é igual ao de cima mas deixa mais automatizado

    def __str__(self): #tipo clase toString
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

#O PRIMEIRO ARGUMENTO É SEMPRE A INSTANCIA DO OBJETO(self)

b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monarkl", 2000, 189)
print(b2)