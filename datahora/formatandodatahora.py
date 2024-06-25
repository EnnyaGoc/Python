#formatar é representar de um jeito especifico pro usuario
#formata com strftime e converte com strptime

from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2024-05-04 16:30"
mascara_ptbr = "%d/%m/%Y %a"
mascara_en = "%Y-%m-%d %H:%M"

print(data_hora_atual.strftime(mascara_ptbr))

data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(data_convertida)
print(type(data_convertida))



#------------------------------------------------------------------
#timezone - fuso horario

#com pytz






#sem pytz