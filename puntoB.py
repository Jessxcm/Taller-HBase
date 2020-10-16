from App import happybase,datetime,messages,users


#PUNTO B
#Actualizar varias veces uno o varios datos de un usuario o mensaje, y recuperar las 3 últimas versiones de ese(os) dato(s)
#users.put(b'jessica@gmail.com',{b'General:Country': b'Argentina'})
#users.put(b'jessica@gmail.com',{b'General:Country': b'Colombia'})

for data in users.cells(b'jessica@gmail.com', b'General:Country', versions=3, include_timestamp=True):
    print (data)