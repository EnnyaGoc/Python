#datetime

import datetime

d = datetime.date(2023, 7, 19)
print(d) # 2023-07-19

# ou from datetime import date
#data = date(2023, 7, 19)
#print(data)

#print(date.today()) data atual




#o datetime.datetime pega a data e hora

from datetime import date, datetime, time

data = date(2023, 7, 19)
print(data)
print(date.today())

data_hora = datetime(2023, 7, 19, 10, 30, 20)
print(data_hora) # 2023-07-19 10:30:20
print(datetime.today()) # 2023-07-19 e horario atual

#time serve p vc construir a hora
hora = time(10, 20, 0)
print(hora) #10:20:00





#----------------------------------------------------------------
#pode usar o timedelta p modificar a data 
import datetime

d = datetime.date(2023, 7, 19, 13, 45)
print(d) # 2023-07-19 13:45:00

#adicionando uam semana
d = d + datetime.timedelta(weeks=1)
print(d) # 2023-07-26 13:45:00


#------------------------------------------------------------------
from datetime import date, datetime, time, timedelta

tipo_carro = "M"
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == "P":
    data_estimada = data_atual - timedelta(days=tempo_pequeno)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
elif tipo_carro == "M":
    data_estimada = data_atual - timedelta(days=tempo_medio)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
else:
    data_estimada = data_atual - timedelta(days=tempo_grande)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")


print(date.today() - timedelta(days=1))

resultado = datetime(2023, 7 , 25 ,10 , 19, 20) - timedelta(hours=1)
print(resultado.time()) #decrementar só a hora 

print(datetime.now().date())