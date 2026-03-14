class Estudiante:
    def __init__(self, nombre, apellido, *notas):
        self.nombre = nombre
        self.apellido = apellido
        self.notas = notas

    def calcular_promedio (self):
        divisor = 0
        suma = 0.0
        lista = self.notas
        for elements in lista:
            divisor += 1
            suma += elements
        return (suma / divisor)

mi_estudiante = Estudiante("Marinano","Simonin", 1.4, 6.2, 7.0, 5,4, 6.3)

print(mi_estudiante.calcular_promedio())
