from validate_docbr import CPF, CNPJ

class Document:

    @staticmethod
    def create_document(document):
        if len(document) == 11:
            return DocCpF(document)
        elif len(document) == 14:
            return DocCnpj(document)
        else:
            raise ValueError("Amount of digits incorrect")

class DocCpF:
    def __init__(self, document):
        if self.validate(document):
            self.cpf = document
        else:
            raise ValueError("Invalid CPF")

    def __str__(self):
        return self.format()

    def validate(self, document):
        validator = CPF()
        return validator.validate(document)

    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)


class DocCnpj:
    def __init__(self, document):
        if self.validate(document):
            self.cnpj = document
        else:
            raise ValueError("Invalid CNPJ")

    def __str__(self):
        return self.format()

    def validate(self, document):
        validator = CNPJ()
        return validator.validate(document)

    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)