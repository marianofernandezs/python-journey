def houl (func, nums):
    return func(nums)

def is_even (val):
    x = 0
    lista = []
    for i in val:
        if i % 2 == 0:
            x += 1
            lista.append(x)

    return lista

x = [1, 2, 3, 4, 5, 7, 8, 10]

print(houl(is_even,x))
