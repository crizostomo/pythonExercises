from cpf_cnpj import Document

#https://sourcemaking.com/design_patterns/factory_method

#Search packages inside pypi

#cpf = "12345678901"
#object_cpf = CPF(cpf)

#print(object_cpf)
example = "39228927879"
#cpf_one = CpF("")
#print(cpf_one)

document = Document.create_document(example)
print(document)