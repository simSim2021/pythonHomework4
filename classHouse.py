# Создайте класс и поля соответствующему вашему варианту (поля статические и динамические).
# Создайте три метода (класса, объекта и статический).
# Выберете поле или метод для реализации инкапсуляции.
# Пропишите запись и считывание (get, set) инкапсулированных полей.

# Вариант 3.Kласс House: id, Номер квартиры, Площадь, Этаж, Количество комнат, Улица, Тип здания, Срок эксплуатации.

import datetime


class House:
    # статические поля
    id = 0
    street = 'Nezavisimosti'

    # конструктор / динамические поля
    def __init__(self, square, floor, qty_rooms, building_type, service_time):
        self.square = square
        self.floor = floor
        self.qty_rooms = qty_rooms
        self.building_type = building_type
        self.service_time = service_time
        House.id += 1

    # метод класса
    @classmethod
    def set_house_id(cls):
        return cls.id

    # метод объекта
    def house_all_info(self):
        print(f"номер квартиры: {self.get_apartment_number()}, площадь: {self.square},"
              f"этаж: {self.floor}, количество комнат: {self.qty_rooms}, улица: {self.street},"
              f"срок эксплуатации с: {self.service_time} года")

    # статический метод
    @staticmethod
    def service_time_calc(service_time):
        return datetime.datetime.now().year - service_time

    # сеттер и геттер для инкапсулированного поля apartment_number

    def set_apartment_number(self, apartment_number):
        self.__apartment_number = apartment_number

    def get_apartment_number(self):
        return self.__apartment_number


# создание 2 объектов класса
first_house = House(45.2, 2, 2, 'block of flats', 1963)
first_house_id = House.set_house_id()   # использование метода класса
second_house = House(61.5, 4, 1, 'town house', 2012)
second_house_id = House.set_house_id()  # использование метода класса

# вывод динамических полей
print('Динамические поля')

print(first_house.__dict__)
print(second_house.__dict__)
print('**************************************************')

# вызов сеттеров для инкапсулированного поля
first_house.set_apartment_number('5')
House.set_apartment_number(second_house, '11')

# использование метода объекта
print('Дом', first_house_id)
first_house.house_all_info()
print('**************************************************')

print('Дом', second_house_id)
House.house_all_info(second_house)
print('**************************************************')

# использование статического метода
print(f'Дом {first_house_id} эксплуатируется ', first_house.service_time_calc(first_house.service_time), 'лет/года')
print(f'Дом {second_house_id} эксплуатируется ', second_house.service_time_calc(second_house.service_time), 'лет/года')
