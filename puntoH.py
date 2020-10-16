from App import happybase,datetime,messages,users,movies
import struct

#PUNTO H
#Encuentre el(los) usuario(s) cuyos mensajes tienen la mayor cantidad de re-envíos.

#Obteniendo la lista de usuarios en la tabla de usuarios

userslist=[]
for key, data in users.scan():
    userslist.append(key)

#print("la cantidad de usuarios es: ",len(userslist))
#print("La lista de usuarios es : ",userslist)


#Obteniendo la cantidad de retweets por usuario
values={}
for i in range(len(userslist)):
    scan_filter = "RowFilter(=,'binaryprefix:"+userslist[i].decode('ascii')+"')"
    retweets_counter=0
    for key, data in messages.scan(columns=['Retweet'],filter=scan_filter):
        #print(key,data)
        retweets_counter+=len(data)
    
    string = "cantidad de retweets de "+userslist[i].decode('ascii') + " : "
    print(string,retweets_counter)
    values[userslist[i].decode('ascii')]=retweets_counter


#Obteniendo los usuarios con maxima cantidad de retweets

print("\n")
print("Usuarios con la maxima cantidad de retweets : ")

for user,retweet in values.items():
    if retweet==max(values.values()):
        print(user)
        print("-----------------")

    