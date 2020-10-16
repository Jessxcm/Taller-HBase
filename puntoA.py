from App import happybase,datetime,messages,users

#PUNTO A
#Listar el texto de los mensajes escritos por usuarios cuyo nombre empieza por ‘d’,’e’, ‘f’,’g’ o ‘h’ (elija las letras que se acomoden a sus datos)

scan_filter = "RowFilter(=,'regexstring:^[d|b|g|o]')" #mensajes de usuarios cuyo nombre empiece por d, b, g u o 

for key, data in messages.scan(columns=['Tweet:content'],filter=scan_filter):
    print (key,data)
    print("----------------")