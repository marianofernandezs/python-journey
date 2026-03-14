class Store:
    def __init__(self, *inventory):
     inventory = list(inventory)
     self.inventory = inventory
     print(type(inventory))

    def add_product (self):
        product = str(input("El nombre del producto que desea agregar: "))
        self.inventory.append(product)
        return self.inventory

    def show_invetory (self):
        return self.inventory





mi_tienda = Store("PS4", "PS5", "Xbox 360", "PS3", "Wii", "Wii U", "Xbox One", "Xbox Series", "Nintendo Switch")


print(mi_tienda.add_product())


print(mi_tienda.show_invetory())
