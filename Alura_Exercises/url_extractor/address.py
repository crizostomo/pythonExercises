import re

address = "Rua das Dalias 227, 127, Parque Internacional, Campo Limpo Paulista, São Paulo, 13223333"

pattern = re.compile("[0-9]{5}[-]?[0-9]{3}")
#? Means that it can appear or not
searching = pattern.search(address)
if searching:
    cep = searching.group()
    print(cep)