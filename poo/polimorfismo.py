#mesmo nome de funçao (mas assinaturas diferentes) sendo usado p tipos diferentes
class Passaro:
    def voar(self):
        print("voando...")

class Pardal(Passaro):
    def voar(self):
        print("pardal pode voar")

class Avestruz(Passaro):
    def voar(self):
        print("avestruz nao pode voar")

#exemplo ruim do uso de herança p ganhar o metodo voar
class Aviao(Passaro):
    def voar(self):
        print("aviao esta decolando...")

def plano_voo(obj):
    obj.voar()

plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())
