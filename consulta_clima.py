import json
import urllib
from urllib import request

#url = 'http://globalmentoring.com.mx/api/clima.json'
#req = request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
#respuesta = urllib.request.urlopen(req)
with open('clima.json', 'r') as file:
    data = file.read()

#print respuesta
#cuerpo_respuesta = respuesta.read()
#procesamos la respuesta json
json_respuesta = json.loads(data)
#print (json_respueta)
# Ejercicio 1. Acceder a la descripción del clima
descripcion_clima = json_respuesta['clima'][0].get('descripcion')

print(f'Descripcion clima: {descripcion_clima}')
# Ejercicio 2. Mostrar la temperatura mínima y  máxima
temp_min = json_respuesta.get('principal').get('temp_min')
print(temp_min)
temp_max = json_respuesta.get('principal').get('temp_max')

