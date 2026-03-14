class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        self.__speed = 0

    def accelerate (self):
        velocity = self.__speed
        velocity += 10
        self.__speed = velocity
        return self.__speed

    def brake (self):
        velocity = self.__speed
        velocity -= 10
        if (velocity < 0):
            return print("Error la velocidad no puede ser negativa")
        self.__speed = velocity
        return self.__speed
    def current_velocity(self):
        return self.__speed

mi_car = Car("Ford", "F-150")

mi_car.accelerate()
mi_car.accelerate()
mi_car.brake()
mi_car.brake()
mi_car.brake()
print(mi_car.current_velocity())

