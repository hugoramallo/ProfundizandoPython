#Profundizar en set
#Un set es una colección de elementos únicos y es mutable
#los elementos de un set deben ser inmutables (no pueden almacenar por ejemplo una lista que es mutable)
#puede contener un string, un entero, un flotante, una tupla
conjunto = {'Juan', True, 18.0}
print(conjunto)

#set vacío incorrecto
conjunto = {} #genera diccionario vacio
print(type(conjunto))
#forma correcta
conjunto = set()
print(conjunto)
print(type(conjunto))

#Mutable
conjunto.add('Juan')
print(conjunto)

#Contiene valores únicos
conjunto.add('Juan') #no se duplicará el valor, solo valores únicos
print(conjunto)

#crear un set a partir de un interable
conjunto = set([4,5,7,8,4]) #se duplica el valor de 4, al convertirlo en un set solo almacenará una vez el 4
print(conjunto)
#podemos agregar más elementos o incluso otro set
conjunto2 = {100,200,300,300}
#agregamos elementos del conjunto 2 al conjunto 1
conjunto.update(conjunto2)
print(conjunto)
#agregamos una lista
conjunto.update([20,30,40,40])
print(conjunto)

#copiar un set a otro set (copia poco profunda, solo las referencias)
conjunto_copia = conjunto.copy()
print(conjunto_copia)

#verificar igualdad sets
print(f'Es igual en contenido? {conjunto == conjunto_copia}') #True
print(f'Es la misma referencia? {conjunto is conjunto_copia}') #False

#Operaciones de conjuntos utilizando sets
#Personas con distintas características
pelo_negro = {'Juan','Karla','Pedro','María'}
pelo_rubio = {'Lorenzo','Laura','Marco'}
ojos_cafe = {'Karla','Laura'}
menores_30 = {'Juan','Karla','María'}

#todos con ojos_cafe y pelo rubio (Unión) (no se repiten los elementos en un set)
print(ojos_cafe.union(pelo_rubio))
#invertir el orden con el mismo resultado (conmutativa)
#el orden no se suele respetar en los sets
print(pelo_rubio.union(ojos_cafe))

# (intersección) Sólo las personas con ojos color café y pelo rubio (conmutativa)
print(ojos_cafe.intersection(pelo_rubio))

#(diferencia / difference) Pelo negro pero sin ojos color café (no es conmutativa)
#personas que se encuentran en el primer set pero no en el segundo
print(pelo_negro.difference(ojos_cafe))

# (diferencia simétrica) Pelo negro u ojos café, pero NO ambos (conmutativa)
#conmutativa es que no importa alterar el orden de los sets
print(pelo_negro.symmetric_difference(ojos_cafe))

#subset (está dentro), superset(lo contiene), disjoint(no tienen nada en común)
pelo_negro = {'Juan','Karla','Pedro','María'}
pelo_rubio = {'Lorenzo','Laura','Marco'}
ojos_cafe = {'Karla','Laura'}
menores_30 = {'Juan','Karla','María'}

#preguntar si un set está contenido en otro (subconjunto)
#revisamos si los elementos del primer conjunto están contenidos en el segundo set
print(menores_30.issubset(pelo_negro)) #True

#preguntar si un set contiene a otro set (superset)
#revisar si los elementos del primer set están contenidos en el segundo set
print(menores_30.issuperset(pelo_negro)) #False


#preguntar si los de pelo negro no tienen pelo rubio (disjoint)
print(pelo_negro.isdisjoint(pelo_rubio)) #true







