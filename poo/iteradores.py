# se a classe tem os metodos __iter__() e __next__() é uma classe iteravel
#__iter__() retorna qual é o obj de iteraçao e o __next__() trata os valores

class MeuIterator:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except IndexError:
            raise StopIteration #para parar a iteraçao
        
for i in MeuIterator(numeros=[1, 2, 3]):
    print(i) # 2, 4, 6


#--------------------------------------------------------------
#geradores - tipos especiais de iteradores e economiza memoria(retorna uma coisa por vez, ocupando menos espaço na memoria)
# retorna valores usando yield ao inves de return

def meu_gerador():
    texto = "python"
    yield texto


for i in meu_gerador():
    print(i)


#com o exemplo de cima

def meu_gerador(numeros: list[int]):
    texto = "python"
    yield texto


for i in meu_gerador():
    print(i)


#vc vai usar o gerador qndo o cod for simples, se for mais complicado, usa o iterador