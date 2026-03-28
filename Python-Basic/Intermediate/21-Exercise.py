#Fizzbuz Excercise

def fizzbuz (num):
    if num % 3 == 0 and num % 5 == 0:
        return "fizzbuz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return num



for i in range(1, 101):
    print(f" \n  {fizzbuz(i)}    \n")


#Anagrama Excercise


def is_anagram (message1, message2):
    if message1.lower() == message2.lower():
        return False
    return sorted(message1.lower()) == sorted(message2.lower())


print(is_anagram("Calo","Cola"))


#Fibonacci


def fibonacci ():
    prev = 0
    next = 1

    for index in range(0,50):
        print(prev)
        fib = prev + next # El proximo numero
        prev = next # Se hace el intercambio
        next = fib



fibonacci()


#Numero Primo

def primo ():
    for num in range (1, 101):

        if num >= 2:

            div = False

            for index in range (2, num):
                if num % index == 0:
                    div = True
                    break
            if not div:
                print(num)

primo()


# Reverse

def reverse(text):

    text_len = len(text)

    reversed_text = ""

    for char in range(0, text_len):

        reversed_text += text[text_len - char - 1]


    return reversed_text


print(reverse("Hola Mundo"))
