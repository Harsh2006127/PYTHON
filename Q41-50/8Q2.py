class Car:
    def __init__(self, brand, model, price, mileage):
        self.brand = brand
        self.model = model
        self.price = price
        self.mileage = mileage

c1 = Car("Toyota", "Fortuner", 4000000, 10)
c2 = Car("Honda", "City", 1500000, 18)

print("Car 1 Details:")
print("Brand:", c1.brand)
print("Model:", c1.model)
print("Price:", c1.price)
print("Mileage:", c1.mileage)

print("\nCar 2 Details:")
print("Brand:", c2.brand)
print("Model:", c2.model)
print("Price:", c2.price)
print("Mileage:", c2.mileage)
