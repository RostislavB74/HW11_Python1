from collections import UserDict


class Car:
    def __init__(self, brand):
        self.brand = brand


class Garage(UserDict):
    def add_car(self, car: Car):
        self.data[car.brand] = car

    def iterator(self, n=3):
        result = []
        counter = 0
        for car in self.data:
            result.append(self.data[car].brand)
            counter += 1
            if counter >= n:
                yield "\n".join(result)
                counter = 0
                result = []
        if result:
            yield "\n".join(result)


if __name__ == "__main__":

    bmw = Car("BMW")
    volvo = Car("Volvo")
    renault = Car("Renault")
    peugeot = Car("Peugeot")

    garage = Garage()

    garage.add_car(bmw)
    garage.add_car(volvo)
    garage.add_car(renault)
    garage.add_car(peugeot)

    for page, car in enumerate(garage.iterator(6), 1):
        print(f"Page {page}")
        print(car)
        input("For next page press any kay")
