class InsufficentFundsError(Exception):
    pass


def transaction (amount):
    balance = 150
    result = int
    try:
        bo = (balance > amount)
        if(bo == False):
            raise InsufficentFundsError
    except InsufficentFundsError:
        return print("Saldo insuficiente ")

    result = balance - amount

    return print(f"El balance es {result}")

user_input = int(input("Ingrese el monto a retirar: "))

call = transaction(user_input)



