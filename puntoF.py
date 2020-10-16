from App import happybase,datetime,messages,users


#PUNTO F
#De acuerdo a la definición de su llave, proponga una consulta que recupere un rango de llaves.


for key, data in users.scan(row_start=b'a', row_stop=b'e'): #usuarios que empiezan por a hasta usuarios que que empiezan por e (sin incluirlos)
    print(key, data)
    print("----------------")

