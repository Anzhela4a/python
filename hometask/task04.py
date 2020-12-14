# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).  А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Выполните вызов методов и также покажите результат.
import random

class Car:
    speed: int
    color: str
    name: str
    is_police = bool
    direction = ['Left', 'Right', 'Around', '']

    def __init__(self, speed, color, name, is_police, direction):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = random.choice(direction)

    def go(self):
        print(f'{self.name} поехал')

    def stop(self):
        print(f'{self.name} остановился')

    def turn(self):
        if self.direction == 'Right':
            print(f'{self.name} повернул направо')
        elif self.direction == 'Left':
            print(f'{self.name} повернул налево')
        elif self.direction == 'Around':
            print(f'{self.name} развернулся')
        else:
            pass

    def show_speed(self):
        print(f'Текущая скорость {self.color} {self.name} составляет {self.speed} км/ч')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police, Car.direction)
    def show_speed(self):
        print(f'Текущая скорость {self.color} {self.name} составляет {self.speed} км/ч')
        if self.speed > 60:
            print(f'Превышение максимально-допустимой скорости на {self.speed - 60} км/ч')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police, Car.direction)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police, Car.direction)
    def show_speed(self):
        print(f'Текущая скорость {self.color} {self.name} составляет {self.speed} км/ч')
        if self.speed > 40:
            print(f'Превышение максимально-допустимой скорости на {self.speed - 40} км/ч')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police, Car.direction)

first_car = TownCar(50, 'black', 'Porsche', False)
second_car = PoliceCar(100, 'wight', 'Ford', True)
third_car = SportCar(130, 'red', 'BMW', False)
fourth_car = WorkCar(50, 'blue', 'Skoda', False)

first_car.go()
first_car.show_speed()
first_car.turn()
first_car.stop()

second_car.go()
second_car.show_speed()
second_car.turn()
second_car.stop()

third_car.go()
third_car.show_speed()
third_car.turn()
third_car.stop()