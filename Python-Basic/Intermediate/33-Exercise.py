def get_other_function(func, val):
    return func(val)

def sum_ten(num):
    return num +10

print(get_other_function(sum_ten, 10))
