import requests
from postCode_access import searchAddress

postCode = "01001000"
object_post_code = searchAddress(postCode)
#print(object_post_code)

#r = requests.get("https://viacep.com.br/ws/01001000/json/")
#print(type(r.text))
#print(r.json())
#print(r.json()['bairro'])

bairro, cidade, uf = object_post_code.access_via_post_code()

print(bairro, cidade, uf)

