def recibe (func, nums):
    return func(nums)

def sum_two (value):
    hola = []
    for i in value:
        x = i + 2
        hola.append(x)
    return hola

x = [1, 4, 6, 8, 10]


print(recibe(sum_two,x))
