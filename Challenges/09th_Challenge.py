#Escribe una función que devuelva los id de las llaves que tienen más de 90 días de antigüedad con respecto a today.

from datetime import datetime, timedelta

# Fecha de hoy simulada para el ejercicio
today = datetime(2024, 5, 1)
# print(type(today))

keys = [
    {"id": "key-1", "created_at": "2024-04-15"}, # Reciente
    {"id": "key-2", "created_at": "2023-10-10"}, # Vieja (> 90 días)
    {"id": "key-3", "created_at": "2024-01-01"}, # Vieja (> 90 días)
] 

def old_ids(keys):
    for date in keys:
#        diferencia = today - (datetime.strptime((date["created_at"]), "%Y-%m-%d"))
        
        diferencia2 = today - (datetime.strptime((date["created_at"]), "%Y-%m-%d"))
        print(diferencia2.days)
        
 #       if (int(str(diferencia).split()[0])) < 90:
        if diferencia2.days < 90:
            return ("reciente")
        else:
            return ("vieja")
print(old_ids(keys))

# arr = map(int, input().split())