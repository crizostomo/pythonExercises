#cityName = input('please type the city"s name')
#DoesItStart = print(cityName[0:5])
#DoesItStart = cityName
#print('Santo' in cityName)


cityName = str(input('please type the city"s name')).strip()
print(cityName[:5].upper() == 'SANTO')


