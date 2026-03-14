class Animal:
    def __init__(self, species):
        self.species = species
    def make_sound (self):
        if self.species.lower() == "gato":
            return f"{self.species} meowwww"
        elif self.species.lower() == "perro":
            return f"{self.species} wauwwww"
        else:
            return f"{self.species} no es un gato ni un perro awww"

mi_animal = Animal("Perro")

print(mi_animal.make_sound())
