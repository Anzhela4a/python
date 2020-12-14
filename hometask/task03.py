class Worker:
    name: str
    surname: str
    position: str
    __income = dict

    def __init__(self, name, surname, position, __income):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = list(__income.values())

class Position (Worker):
    def __init__(self, name, surname, position, __income):
        super().__init__(name, surname, position, __income)

    def get_full_name(self):
        print(f'{self.name} {self.surname} - {self.position}')

    def get_total_income(self):
        print(sum(self._Worker__income))

john = Position('Andrew', 'Dowson', 'engeneer', {'wage': 12000, 'bonus': 5000})
john.get_full_name()
john.get_total_income()
