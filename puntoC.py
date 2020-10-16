from App import happybase,datetime,messages,users

#PUNTO C
#Listar los datos de los usuarios que en sus mensajes han incluido la palabra “Colombia” (elija una palabra que se acomode a sus datos)
#----------------------------------


scan_filter = "SingleColumnValueFilter('Tweet','content',=,'regexstring:Colombia', true,true)"

for key, data in messages.scan(filter=scan_filter):
    print (key,data)
    print("----------------")