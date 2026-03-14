class Animal:
    def __init__(self, species):
        self.species = species
    def make_sound (self):
        return f"{self.species} arrrrr"


mi_animal = Animal("Tigre")

print(mi_animal.make_sound())
