from App import happybase,datetime,messages,users


#PUNTO G
#Encuentre el promedio de mensajes que cada usuario escribe por mes

#cantidad de mensajes por mes
months={
    'Enero':0,
    'Febrero':0,
    'Marzo':0,
    'Abril':0,
    'Mayo':0,
    'Junio':0,
    'Julio':0,
    'Agosto':0,
    'Septiembre':0,
    'Octubre':0,
    'Noviembre':0,
    'Diciembre':0
}

#Obteniendo la cantidad de mensajes por mes
for key, data in messages.scan():
    string=key.decode("utf-8") 
    fechastring=string[-19:]
    fechadate=datetime.strptime(fechastring, '%Y-%m-%d %H:%M:%S')
    month = int(fechadate.strftime('%m'))
    if month==1:
        months['Enero']+=1
    elif month==2:
        months['Febrero']+=1
    elif month==3:
        months['Marzo']+=1
    elif month==4:
        months['Abril']+=1
    elif month==5:
        months['Mayo']+=1
    elif month==6:
        months['Junio']+=1
    elif month==7:
        months['Julio']+=1
    elif month==8:
        months['Agosto']+=1
    elif month==9:
        months['Septiembre']+=1
    elif month==10:
        months['Octubre']+=1
    elif month==11:
        months['Noviembre']+=1
    else:
        months['Diciembre']+=1
    
#print(months)


#Obteniendo la lista de usuarios en la tabla de usuarios

userslist=[]
for key, data in users.scan():
    userslist.append(key)


#print("la cantidad de usuarios es: ",len(userslist))
#print("La lista de usuarios es : ",userslist)


def safe_div(x,y):
    if y == 0:
        return 0
    return x / y


#PROMEDIO DE T POR USUARIO

print("-----------------------------------------------")
print("CALCULANDO EL PROMEDIO DE TWEETS POR USUARIO")
print("-----------------------------------------------")

#promedio de mensajes por usuario al mes
for i in range(len(userslist)):
    scan_filter = "RowFilter(=,'binaryprefix:"+userslist[i].decode('ascii')+"')"
    tweets_counter=0

    months_user={
    'Enero':0,
    'Febrero':0,
    'Marzo':0,
    'Abril':0,
    'Mayo':0,
    'Junio':0,
    'Julio':0,
    'Agosto':0,
    'Septiembre':0,
    'Octubre':0,
    'Noviembre':0,
    'Diciembre':0
    }


    for key, data in messages.scan(filter=scan_filter):
        #obteniendo el mes
        string=key.decode("utf-8") 
        fechastring=string[-19:]
        fechadate=datetime.strptime(fechastring, '%Y-%m-%d %H:%M:%S')
        month = int(fechadate.strftime('%m'))
        
        if month==1:
            months_user['Enero']+=1
        elif month==2:
            months_user['Febrero']+=1
        elif month==3:
            months_user['Marzo']+=1
        elif month==4:
            months_user['Abril']+=1
        elif month==5:
            months_user['Mayo']+=1
        elif month==6:
            months_user['Junio']+=1
        elif month==7:
            months_user['Julio']+=1
        elif month==8:
            months_user['Agosto']+=1
        elif month==9:
            months_user['Septiembre']+=1
        elif month==10:
            months_user['Octubre']+=1
        elif month==11:
            months_user['Noviembre']+=1
        else:
            months_user['Diciembre']+=1
    
    #string = "cantidad de tweets de "+userslist[i].decode('ascii') + " por mes : "
    #print(string,months_user)

    avg_month={
    'Enero':0,
    'Febrero':0,
    'Marzo':0,
    'Abril':0,
    'Mayo':0,
    'Junio':0,
    'Julio':0,
    'Agosto':0,
    'Septiembre':0,
    'Octubre':0,
    'Noviembre':0,
    'Diciembre':0
    }

    #el promedio es: cantidad de mensajes del usuario / cantidad de mensajes en el mes
    for month,value in months_user.items():
        if month=='Enero':
            avg_month['Enero']=safe_div(months_user['Enero'],months['Enero'])
        elif month=='Febrero':
            avg_month['Febrero']=safe_div(months_user['Febrero'],months['Febrero'])
        elif month=='Marzo':
            avg_month['Marzo']=safe_div(months_user['Marzo'],months['Marzo'])
        elif month=='Abril':
            avg_month['Abril']=safe_div(months_user['Abril'],months['Abril'])
        elif month=='Mayo':
            avg_month['Mayo']=safe_div(months_user['Mayo'],months['Mayo'])
        elif month=='Junio':
            avg_month['Junio']=safe_div(months_user['Junio'],months['Junio'])
        elif month=='Julio':
            avg_month['Julio']=safe_div(months_user['Julio'],months['Julio'])
        elif month=='Agosto':
            avg_month['Agosto']=safe_div(months_user['Agosto'],months['Agosto'])
        elif month=='Septiembre':
            avg_month['Septiembre']=safe_div(months_user['Septiembre'],months['Septiembre'])
        elif month=='Octubre':
            avg_month['Octubre']=safe_div(months_user['Octubre'],months['Octubre'])
        elif month=='Noviembre':
            avg_month['Noviembre']=safe_div(months_user['Noviembre'],months['Noviembre'])
        else:
            avg_month['Diciembre']=safe_div(months_user['Diciembre'],months['Diciembre'])

    string = "El promedio de tweets del usuario "+userslist[i].decode('ascii') + " por mes es: "
    print(string,avg_month)
    print("-----------------------------------------------")




    