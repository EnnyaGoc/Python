import requests
import json

cotacoes = requests.get(" https://economia.awesomeapi.com.br/json/last/:moedas") #pegando o api
cotacoes = cotacoes.json() #transformando em formato json
print(cotacoes)

