#leer contenido online de una web
from urllib.request import urlopen

palabras = []
with urlopen('http://globalmentoring.com.mx/recursos/GlobalMentoring.txt') as mensaje:
    for linea in mensaje:
        #recuperamos cada palabra que tenemos en la lista
        palabras_por_linea = linea.decode('utf-8').split()
        for palabra in palabras_por_linea:
            palabras.append(palabra)
    #leemos el archivo y lo decodificamos en utf8
    #contenido = mensaje.read().decode('UTF-8')
    #print(contenido)

#creamos un nuevo archivo txt para copiar la información del archivo online
#with open('nuevo_archivo.txt','w', encoding='utf-8') as archivo:
    #escribimos en el nuevo archivo
    #archivo.write(contenido)

