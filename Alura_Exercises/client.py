class Client:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        print("calling @property name")
        return self.__name.title()

    @name.setter
    def name(self, name):
        self.__name = name
        print("calling setter name")
        self.__name = name


