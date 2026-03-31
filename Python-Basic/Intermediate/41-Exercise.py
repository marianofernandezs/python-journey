#SyntaxError

#print "Hola como estas" # Genera un SyntaxError

#NameError

#print(sport) # Genera un NameError

# IndexError

my_list = [1,2,3,4]

#print(my_list[7]) # Genera un IndexError

# ModuleNotFoundError

#import hola # Genera un ModuleNotFoundError

#AttributeError

x = ""
#print(x.len()) #Genera un AttributeError

#KeyError

my_dict = {"Nombre": "Mariano","Nivel": 1, "Languages": "Spanish , English"}

#print(my_dict["hola"]) #Genera un KeyError

# TypeError

#print(my_list["0"]) #Genera un TypeError

#ImportError
#from math import PIS #Genera un ImportError

#ValueError

#number = int("10 years")# Genera un ValueError

#print(number)

my_dict = {"Nombre": "Mariano","Nivel": 1, "Languages": "Spanish , English"}

try:
    print(my_dict["hola"])
except KeyError:
    print("Clave no encontrada")
