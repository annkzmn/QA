# Создайте любой класс
# с произвольным количеством подклассов, экземпляров, атрибутов и методов - как минимум один атрибут должен быть с уровнем
# доступа private.Соответственно, для получения значений этого атрибута нужно использовать методы get и set
#
# Этот класс Car имеет закрытый (приватный) атрибут _mileage, который можно получить и установить с
# использованием методов get_mileage и set_mileage. Класс также имеет другие методы для работы с машиной,
# такие как drive и display_info

class Car:
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self._mileage = mileage  # Атрибут _mileage с уровнем доступа private

    def get_mileage(self):
        return self._mileage

    def set_mileage(self, mileage):
        if mileage >= 0:
            self._mileage = mileage
        else:
            print("Недопустимое значение пробега")

    def drive(self, miles):
        if miles > 0:
            self._mileage += miles
        else:
            print("Недопустимое значение расстояния")

    def display_info(self):
        print(f"Марка: {self.make}")
        print(f"Модель: {self.model}")
        print(f"Год выпуска: {self.year}")
        print(f"Пробег: {self._mileage} миль")

# Создаем экземпляр класса Car
my_car = Car("Toyota", "Camry", 2020, 20000)

# Используем методы get и set для атрибута _mileage
print("Пробег:", my_car.get_mileage())
my_car.set_mileage(22000)
print("Пробег после установки:", my_car.get_mileage())

# Изменяем пробег с помощью метода drive
my_car.drive(100)
print("Пробег после поездки:", my_car.get_mileage())

# Выводим информацию о машине
my_car.display_info()
