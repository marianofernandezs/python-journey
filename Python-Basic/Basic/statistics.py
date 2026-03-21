def calculate_mediana (nums):
    contador = 0
    for element in nums:
        contador += 1
    
    nums.sort()

    print(f"la lista ordenada {nums}")

    if contador % 2 == 0:
        position = (contador + 1) // 2
        print(f"{position}")
        position1 = position - 1
        position2 = position + 1
        value1 = nums[position1]
        value2 = nums[position2]

        mediana = (value1+value2) / 2

        return print(f"La mediana es {mediana}")
        


    else:
        position = (contador + 1)// 2
        mediana = nums[position]
        return print(f"La mediana es {mediana}")



