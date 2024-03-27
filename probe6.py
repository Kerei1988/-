class Car:
    price = 1000000
    power = 100

    def __init__(self, price):
        self.price = price

    def horse_powers(self):
        return self.power


class Nissan(Car):
    def __init__(self, price):
        Car.__init__(self, price)

    def horse_powers(self):
        Car.horse_powers(self)

class Kia(Car):
    def __init__(self, price):
        Car.__init__(self, price)

    def horse_powers(self):
        Car.horse_powers(self)



my_car = Car
my_car.horse_powers = 300
my_car.price = 1500000
print(my_car.horse_powers, my_car.price)

son_car = Nissan
son_car.horse_powers = 200
son_car.price = 800000
print(son_car.horse_powers, son_car.price)

wife_car = Kia
wife_car.price = 1000000
wife_car.horse_powers = 150
print(wife_car.horse_powers, wife_car.price)


print(wife_car.price is Car.price)