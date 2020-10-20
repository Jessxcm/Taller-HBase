#-------------------------------------------------------------------------------------------------------------------------------
#INGRESO DE DATOS
#-------------------------------------------------------------------------------------------------------------------------------
#TIPOS DE DE MENSAJES: 1 TWEET, 2 RETWEET, 3 RESPONSE
#connection.create_table('msgsXusr',{'tweet':dict()})
#menxusuarios.put('jessica@gmail.com|2020-01-01 09:28:35',{'tweet:tipo': '1', 'tweet:contenido':'Mi primer mensaje en esta red social', 'tweet:usr':'jessica@gmail.com'}, timestamp=123456789)
#menxusuarios.put('jessica@gmail.com|2020-01-02 22:28:35',{'tweet:tipo': '2', 'tweet:contenido':'Mi primer mensaje en esta red social', 'tweet:usr':'diego@gmail.com'}, timestamp=123456789)
#menxusuarios.put('jessica@gmail.com|2020-08-02 10:28:35',{'tweet:tipo': '3', 'tweet:contenido':'Felicitaciones, lo lograste', 'tweet:usr':'diego@gmail.com'}, timestamp=123456789)
#menxusuarios.put('diego@gmail.com|2020-04-02 22:28:35',{'tweet:tipo': '1', 'tweet:contenido':'Bienvenidos a mi perfil', 'tweet:usr':'diego@gmail.com'}, timestamp=123456789)
#menxusuarios.put('diego@gmail.com|2020-04-02 23:28:35',{'tweet:tipo': '2', 'tweet:contenido':'vamos de vacaciones', 'tweet:usr':'elena@gmail.com'}, timestamp=123456789)
#menxusuarios.put('elena@gmail.com|2020-05-02 11:28:35',{'tweet:tipo': '1', 'tweet:contenido':'Amo la vida', 'tweet:usr':'elena@gmail.com'}, timestamp=123456789)
#menxusuarios.put('elena@gmail.com|2020-06-06 14:28:35',{'tweet:tipo': '3', 'tweet:contenido':'la vida es bella', 'tweet:usr':'jessica@gmail.com'}, timestamp=123456789)
#menxusuarios.put('jessica@gmail.com|2020-09-19 13:28:35',{'tweet:tipo': '1', 'tweet:contenido':'Quiero hamburguesa', 'tweet:usr':'jessica@gmail.com'}, timestamp=123456789)
#menxusuarios.put('jessica@gmail.com|2020-02-11 13:28:35',{'tweet:tipo': '1', 'tweet:contenido':'me gusta hbase', 'tweet:usr':'jessica@gmail.com'}, timestamp=123456789)
#menxusuarios.put('jessica@gmail.com|2020-03-12 14:28:35',{'tweet:tipo': '1', 'tweet:contenido':'me gusta python', 'tweet:usr':'jessica@gmail.com'}, timestamp=123456789)
#menxusuarios.put('jessica@gmail.com|2020-06-13 15:28:35',{'tweet:tipo': '1', 'tweet:contenido':'me gusta SQL', 'tweet:usr':'jessica@gmail.com'}, timestamp=123456789)
#menxusuarios.put('jessica@gmail.com|2020-07-14 16:28:35',{'tweet:tipo': '2', 'tweet:contenido':'vacaciones a san andres', 'tweet:usr':'diego@outlook.es'}, timestamp=123456789)
#menxusuarios.put('jessica@gmail.com|2020-03-15 17:28:35',{'tweet:tipo': '2', 'tweet:contenido':'juego minecraft', 'tweet:usr':'efren@javerianacali.edu.co'}, timestamp=123456789)
#menxusuarios.put('jessica@gmail.com|2020-10-16 18:28:35',{'tweet:tipo': '2', 'tweet:contenido':'Quiero chuleta', 'tweet:usr':'kfaley9@yahoo.com'}, timestamp=123456789)
#menxusuarios.put('jessica@gmail.com|2020-09-17 19:28:35',{'tweet:tipo': '3', 'tweet:contenido':'Yo tambien', 'tweet:usr':'diego@outlook.es'}, timestamp=123456789)
#menxusuarios.put('jessica@gmail.com|2020-09-18 11:28:35',{'tweet:tipo': '3', 'tweet:contenido':'me gusta LoL', 'tweet:usr':'efren@javerianacali.edu.co'}, timestamp=123456789)
#menxusuarios.put('diego@outlook.es|2020-05-19 13:28:35',{'tweet:tipo': '1', 'tweet:contenido':'Vacaciones a Francia', 'tweet:usr':'diego@outlook.es'}, timestamp=123456789)
#menxusuarios.put('diego@outlook.es|2020-04-08 14:28:35',{'tweet:tipo': '1', 'tweet:contenido':'Vacaciones a Italia', 'tweet:usr':'diego@outlook.es'}, timestamp=123456789)
#menxusuarios.put('diego@outlook.es|2020-10-20 15:28:35',{'tweet:tipo': '2', 'tweet:contenido':'Mi primer mensaje en esta red social', 'tweet:usr':'jessica@gmail.com'}, timestamp=123456789)
#menxusuarios.put('diego@outlook.es|2019-12-15 16:28:35',{'tweet:tipo': '2', 'tweet:contenido':'Juego Roblox', 'tweet:usr':'efren@javerianacali.edu.co'}, timestamp=123456789)
#menxusuarios.put('diego@outlook.es|2020-01-12 17:28:35',{'tweet:tipo': '3', 'tweet:contenido':'Vacaciones a Argentina', 'tweet:usr':'jessica@gmail.com'}, timestamp=123456789)
#menxusuarios.put('diego@outlook.es|2020-01-13 18:28:35',{'tweet:tipo': '3', 'tweet:contenido':'Vacaciones a Hawaii', 'tweet:usr':'kfaley9@yahoo.com'}, timestamp=123456789)
#menxusuarios.put('diego@outlook.es|2020-03-25 19:28:35',{'tweet:tipo': '1', 'tweet:contenido':'Vacaciones a San Andres', 'tweet:usr':'diego@outlook.es'}, timestamp=123456789)
#menxusuarios.put('efren@javerianacali.edu.co|2020-01-19 13:28:35',{'tweet:tipo': '1', 'tweet:contenido':'Juego Roblox', 'tweet:usr':'efren@javerianacali.edu.co'}, timestamp=123456789)
#menxusuarios.put('efren@javerianacali.edu.co|2020-02-19 13:28:35',{'tweet:tipo': '1', 'tweet:contenido':'Juego LoL', 'tweet:usr':'efren@javerianacali.edu.co'}, timestamp=123456789)
#menxusuarios.put('efren@javerianacali.edu.co|2020-03-19 13:28:35',{'tweet:tipo': '2', 'tweet:contenido':'Vacaciones a Francia', 'tweet:usr':'diego@outlook.es'}, timestamp=123456789)
#menxusuarios.put('efren@javerianacali.edu.co|2020-04-19 13:28:35',{'tweet:tipo': '2', 'tweet:contenido':'Vacaciones a San Andres', 'tweet:usr':'diego@outlook.es'}, timestamp=123456789)
#menxusuarios.put('efren@javerianacali.edu.co|2020-05-19 13:28:35',{'tweet:tipo': '3', 'tweet:contenido':'Juego Brawl Stars', 'tweet:usr':'jessica@gmail.com'}, timestamp=123456789)
#menxusuarios.put('efren@javerianacali.edu.co|2019-11-19 13:28:35',{'tweet:tipo': '3', 'tweet:contenido':'Juego Fortnite', 'tweet:usr':'kfaley9@yahoo.com'}, timestamp=123456789)
#menxusuarios.put('efren@javerianacali.edu.co|2019-12-19 13:28:35',{'tweet:tipo': '1', 'tweet:contenido':'Juego Pokemon GO', 'tweet:usr':'efren@javerianacali.edu.co'}, timestamp=123456789)
#menxusuarios.put('kfaley9@yahoo.com|2020-11-19 13:28:35',{'tweet:tipo': '1', 'tweet:contenido':'Quiero Perro', 'tweet:usr':'kfaley9@yahoo.com'}, timestamp=123456789)
#menxusuarios.put('kfaley9@yahoo.com|2020-09-19 13:28:35',{'tweet:tipo': '1', 'tweet:contenido':'Quiero Pizza', 'tweet:usr':'kfaley9@yahoo.com'}, timestamp=123456789)
#menxusuarios.put('kfaley9@yahoo.com|2020-10-19 13:28:35',{'tweet:tipo': '2', 'tweet:contenido':'Vacaciones a Italia', 'tweet:usr':'diego@outlook.es'}, timestamp=123456789)
#menxusuarios.put('kfaley9@yahoo.com|2020-10-19 13:28:35',{'tweet:tipo': '2', 'tweet:contenido':'Quiero hamburguesa', 'tweet:usr':'jessica@gmail.com'}, timestamp=123456789)
#menxusuarios.put('kfaley9@yahoo.com|2020-03-19 13:28:35',{'tweet:tipo': '3', 'tweet:contenido':'Quiero chuleta', 'tweet:usr':'efren@javerianacali.edu.co'}, timestamp=123456789)
#menxusuarios.put('kfaley9@yahoo.com|2020-08-19 13:28:35',{'tweet:tipo': '3', 'tweet:contenido':'Quiero bisteck', 'tweet:usr':'efren@javerianacali.edu.co'}, timestamp=123456789)
#menxusuarios.put('kfaley9@yahoo.com|2020-01-19 13:28:35',{'tweet:tipo': '1', 'tweet:contenido':'Quiero cuy', 'tweet:usr':'kfaley9@yahoo.com'}, timestamp=123456789)

import happybase
from datetime import datetime
connection = happybase.Connection(table_prefix="bd03:",table_prefix_separator=b'')
connection.open()
messages = connection.table('Messages')
users = connection.table('Users')
menxusuarios = connection.table('msgsXusr')

#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
#ENTRADA A LA APLICACIÓN
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------

#PUNTO 1
#Los últimos 10 mensajes que el usuario ha publicado, en orden cronológico, empezando por el más reciente. 
# Si son réplicas, indica el mensaje original y el usuario que lo publicó. 
# Si son mensajes re-enviados, indica el usuario que publicó el mensaje original.

scan_filter = "RowFilter(=,'binaryprefix:jessica@gmail.com')"
print ("-------------------------------------------------------------------------------------------------------------------------")
print ("MIS MENSAJES")
print ("-------------------------------------------------------------------------------------------------------------------------")
for key, data in menxusuarios.scan(columns=['tweet:contenido','tweet:usr'],filter=scan_filter,reverse=True,limit=10):
    print(key,data)
print ("-------------------------------------------------------------------------------------------------------------------------")

#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------

#PUNTO 2
#Los últimos 5 mensajes que han publicado cada uno de los usuarios a los que sigue, agrupados por el usuario que los publica.
# Los usuarios deben estar en orden alfabético y, los mensajes de cada usuario, en orden cronológico, empezando por el más reciente.

row = users.row('jessica@gmail.com', columns=['Following'])

llaves = row.keys()
for element in llaves:
    seguido = element[10:]
    str_seguido = seguido.decode("utf-8") 
    print ("-------------------------------------------------------------------------------------------------------------------------")
    print('USUARIO: ', str_seguido)
    print ("-------------------------------------------------------------------------------------------------------------------------")
    #scan_filter = "RowFilter(=,'binaryprefix:jessica@gmail.com')"
    scan_filter = "RowFilter(=,'binaryprefix:" + str_seguido + "')"
    for key, data in menxusuarios.scan(columns=['tweet:contenido','tweet:usr'],filter=scan_filter,reverse=True,limit=5):
        print(key,data)

print ("-------------------------------------------------------------------------------------------------------------------------")