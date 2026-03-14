def arbitrary_sum (*numbers):
    numbers = list(numbers)
    result = 0
    for number in numbers:
        result += number
    return result

operation = arbitrary_sum(1,7,9,10,100)

print(operation)
