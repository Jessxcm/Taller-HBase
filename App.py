import happybase
from datetime import datetime
connection = happybase.Connection(table_prefix="bd03:",table_prefix_separator=b'')

messages = connection.table('Messages')
users = connection.table('Users')


#ENTRADA A LA APLICACIÓN
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------

#PUNTO 1
#Los últimos 10 mensajes que el usuario ha publicado, en orden cronológico, empezando por el más reciente. 
# Si son réplicas, indica el mensaje original y el usuario que lo publicó. 
# Si son mensajes re-enviados, indica el usuario que publicó el mensaje original.

scan_filter = "RowFilter(=,'binaryprefix:jessica@gmail.com')"

for key, data in messages.scan(filter=scan_filter,reverse=True,limit=10):
    print(key,data)

    #string=key.decode("utf-8") 
    #fechastring=string[-19:]
    #fechadate=datetime.strptime(fechastring, '%Y-%m-%d %H:%M:%S')
    #print("Fecha es: ",fechadate)
    print ("---------")

#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------


#PUNTO 2
#Los últimos 5 mensajes que han publicado cada uno de los usuarios a los que sigue, agrupados por el usuario que los publica.
# Los usuarios deben estar en orden alfabético y, los mensajes de cada usuario, en orden cronológico, empezando por el más reciente.
