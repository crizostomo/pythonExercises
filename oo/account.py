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

    def __can_withdraw(self, value_to_withdraw):
        value_available_to_withdraw = (self.__balance + self.__limit)
        return value_to_withdraw <= value_available_to_withdraw

    def withdraw(self, value):
        if(self.__can_withdraw(value)):
            self.__balance -= value
        else:
            print("The value {} surpassed the limit".format(value))

    def transfer(self, value, destination):
        self.withdraw(value)
        destination.deposit(value)

    @property
    def balance(self):
        return self.__balance

    @property
    def holder(self):
        return self.__holder

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, limit):
        self.__limit = limit

    @staticmethod
    def code_bank():
        return {'BB':'001', 'Bradesco':'237'}