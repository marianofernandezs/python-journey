class Book:
    def __init__(self,title,author):
        self.title = title
        self.__author = author
    def get_author(self):
        return self.__author
    def change_title (self):
        new_title = str(input("Ingrese el nuevo titulo: "))
        self.title = new_title
        return self.title


mi_libro = Book("Mi libro luna de pluton", "Dross")

print(mi_libro.get_author() + f"es el autor del libro {mi_libro.title} ")

mi_libro.change_title()

print(mi_libro.title)
        
