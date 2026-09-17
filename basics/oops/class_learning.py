class Car:
    # init is just normal function and it is like constructor
    def __init__(self,brand, name): # self is like this keyword
        # self.__price = price private memeber
        self.brand = brand
        self.name = name

    def full_name(self):
        return f"{self.brand} {self.name}" #f"" return the formated string


# inherited class
# super will get the access to passed class
class ElectricCar(Car):
    def __init__(self, brand, name, batter_size):
        super().__init__(brand, name)
        self.batter_size = batter_size

my_car = Car('cadilac', 'escalade')
print(my_car.brand)
print(my_car.full_name())

my_electric_car = Car('Gwagon', 'g65')
print(my_electric_car.brand)
print(my_electric_car.full_name())