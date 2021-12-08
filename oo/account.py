class Account:

    def __init__(self, number, holder, balance, limit):
        print("Building object...{}".format(self))
        self.__number = number
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit

    def bank_statement(self):
        print("The balance of the holder {} is {}".format(self.__holder, self.__balance))

    def deposit(self, value):
        self.__balance += value

    def withdraw(self, value):
        self.__balance -= value