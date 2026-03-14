class Bank:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def withdraw_money (self):
        print(f"Tu balance es {self.balance}")
        withdraw = int(input("Ingresa cuanto quieres sacar: "))
        balance = self.balance - withdraw

        if balance < 0:
            return "Operacion invalida, no puede haber balance negativo"
        self.balance = balance

        return self.balance
    def deposit_money (self):
        print(f"Tu balance es {self.balance}")
        deposit = (int(input("Ingresa cuanto quieres depositar: ")))
        self.balance = self.balance + deposit
        return self.balance

mi_banco = Bank("Mariano", 140)

print(mi_banco.withdraw_money())

print(mi_banco.deposit_money())

print(mi_banco.withdraw_money())


