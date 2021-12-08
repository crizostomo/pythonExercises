def create_account(number, holder, balance, limit):
    account = {"number": number, "holder": holder, "balance": balance, "limit": limit}
    return account

def deposit(account, value):
    account["balance"] += value

def withdraw(account, value):
    account["balance"] -= value

def bank_statement(account):
    print("The balance is {}".format(account["balance"]))