from App import happybase,datetime,messages,users

#PUNTO E
#Proponga una consulta cuya expresión incluya un filtro que use al menos 3 funciones distintas.

#scan_filter = "SingleColumnValueFilter('General','Year',=,'binary:2001', true,true) OR SingleColumnValueFilter('General','Year',=,'binary:1968', true,true)"

scan_filter = "RowFilter(=,'regexstring:^[k]') AND SingleColumnValueFilter('General','Country',=,'binary:United States', true,true) AND SingleColumnValueFilter('General','Profile_type',=,'binary:private', true,true)"


for key, data in users.scan(filter=scan_filter):
    print(key, data)
    print("----------------")