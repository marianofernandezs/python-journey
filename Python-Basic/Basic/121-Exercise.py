def operations (operation, number_one, number_two):
    if operation == 1:
        return print(number_one + number_two)
    elif operation == 2:
        return print(number_one - number_two)
    elif operation == 3:
        return print(number_one * number_two)
    elif operation == 4:
        try:
            result = number_one // number_two
            return print(result)
        except ZeroDivisionError:
            return print("Cannot divide in 0")
    else:
        print("The operation selected not exist")

def print_menu ():
    header = print("The Menu ")
    op1 = print("1.- Sum")
    op2 = print("2.- Substraction")
    op3 = print("3.- Multpication")
    op4 = print("4.- Division")
    return (f"{header} \n {op1} \n {op2} \n {op3} \n {op4}")


print_menu()

while True:
    try:
        op = int(input("Enter the operation: "))
        number_one = int(input("Enter the first number: "))
        number_two = int(input("Enter the second number: "))
        
        operation_call = operations(op,number_one,number_two)

        break
    except ValueError:
        print("You cannot string or float")
