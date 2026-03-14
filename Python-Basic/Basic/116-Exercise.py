class Employee:
    def __init__(self, name, hourly_wage, hours_worked):
        self.name = name
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked

    def payment (self):
        return self.hourly_wage * self.hours_worked



mi_empleado = Employee("Mariano",15, 80)

print(mi_empleado.payment())
        
