def multiply_number (num):
    if num % 2 != 0:
        return num * 3
    else:
        return num

numbers = [1, 2, 3, 6, 7, 8, 9, 13, 15, 16, 17]

my_list = [multiply_number(i) for i in numbers]

print(my_list)
