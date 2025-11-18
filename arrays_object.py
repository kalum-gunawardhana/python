from array import array
numbers = [10, 20, 30, 40]
print(numbers[0])   # 10

fruits = ["apple", "banana", "mango"]
fruits.append("orange")
print(fruits)


numbers = array('i', [1, 2, 3, 4])  # 'i' → integer type
print(numbers)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Kalum", 25)

print(p1.name)  # Kalum
print(p1.age)   # 25


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        print(self.brand, self.model)


car1 = Car("Toyota", "Corolla")
car1.info()


person = {
    "name": "Kalum",
    "age": 25,
    "city": "Colombo"
}

print(person["name"])


person["age"] = 26


person["job"] = "Engineer"
