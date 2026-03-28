
numbers = [1, 2, 4, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]

def grather_than_ten (num):
    if num > 10:
        return True
    else:
        return False


my_list = [grather_than_ten(i) for i in numbers]

print (my_list)
