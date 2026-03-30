def recibi (func1, func2, num):
    return func1(func2(num))

def elevate (func2):
    return func2**2

def sum_ten (func1):
    return func1+10

print(recibi(elevate, sum_ten, 10))
