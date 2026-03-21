def age ():
    age = int
    while True:
        try:
            age = int(input("Enter your age: "))
            age = age.__abs__()
            break
        except ValueError:
            print ("Your age cannot be a string")
    return print(f"Your age is {age}")


age()
