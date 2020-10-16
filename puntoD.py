from App import happybase,datetime,messages,users

#PUNTO D
#Listar los mensajes que incluyen una URL con la siguiente estructura: protocol://subdomain.domain.top-level-domain
#Donde, protocol puede ser http, https, mailto, o ftp; subdomain, domain, y top-level-domain son cadenas que incluyen letras, números y guión (-).

scan_filter = "SingleColumnValueFilter('Tweet','content',=,'regexstring:(http|https|ftp|mailto)://[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+\.[a-zA-Z0-9-]', true,true)"

for key, data in messages.scan(filter=scan_filter):
    print (key,data)
    print("----------------")