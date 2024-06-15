#n tem uma palavra reservara p interface mas tem herança multipla, entao pode fazer com q outras classes herdem da classe abstrata

#n fornece classe abstrata entao fornece o modulo ABC pra definir elas
#o metodfo se torna abstrato qndo usa o @abstractmethod

from abc import ABC, abstractmethod, abstractproperty


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractmethod
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")
        print("Ligada!")

    def desligar(self):
        print("Desligando a TV...")
        print("Desligada!")

    @property
    def marca(self):
        return "Philco"


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o ar condicionado...")

    def desligar(self):
        print("Desligando o ar condicionado...")

    @property
    def marca(self):
        return "LG"
    
    
controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)


controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)