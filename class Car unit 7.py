class Car:
    def __init__(self):
        self.cars = {
            "Toyota": {
                "Corolla": {
                    "year": 2021,
                    "color": "red",
                    "price": 20000
                },
                "Camry": {
                    "year": 2022,
                    "color": "blue",
                    "price": 25000
                }
            },
            "Honda": {
                "Civic": {
                    "year": 2021,
                    "color": "black",
                    "price": 22000
                },
                "Accord": {
                    "year": 2022,
                    "color": "white",
                    "price": 28000
                }
            }
        }

    def display_cars(self):
        print("Cars:")
        for make, models in self.cars.items():
            print(f"{make}:")
            for model, details in models.items():
                print(f"  {model}: {details}")

    def display_car_makes(self):
        print("Car Makes:")
        for make in self.cars.keys():
            print(f"- {make}")

    def display_car_details(self):
        print("Car Details:")
        for details in self.cars.values():
            for model in details.keys():
                print(f"- {model}: {details[model]}")


car = Car()
car.display_cars()
print()
car.display_car_makes()
print()
car.display_car_details()
