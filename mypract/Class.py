''' Задание с телефоном № 1
class Phone:
    def __init__(self, model, number):
        self.model = model
        self.number = number

    def display_info(self):
        print(f"Model: {self.model}  Number: {self.number}")


    def cell(self):
        print(f"Идёт звонок на {self.number}")


Samsung = Phone("S24+", 8700666666)
Samsung.display_info()
Samsung.cell()

Google = Phone("Pixel 8 pro", 87000000)
Google.display_info()
Google.cell()
'''

''' Задание № 2 Машинки
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        self.country_of_origin = {
            "Toyota": "JAPAN",
            "Tesla": "USA",
            "Lada": "Russia"
        }

    def country(self):
        country = self.country_of_origin.get(self.brand, "Неизвестно")
        print(f"Страна производитель: {country}")


car1 = Car("Toyota", 2025)
car2 = Car("Tesla", 2023)
car3 = Car("Lada", 2022)

print(f"Бренд: {car1.brand}, Год: {car1.year}")
car1.country()

print(f"Бренд: {car2.brand}, Год: {car2.year}")
car2.country()

print(f"Бренд: {car3.brand}, Год: {car3.year}")
car3.country()
'''

class Calculator:

    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2


    def plus(self):
        result = self.number1 + self.number2
        print(f"Результат сложения: {result}")


    def minis(self):
        result = self.number1 - self.number2
        print(f"Результат вычитания: {result}")

    def mult(self):
        result = self.number1 * self.number2
        print(f"Результат умножения: {result}")


result = Calculator(14, 88 )
result.plus()
result.minis()
result.mult()




