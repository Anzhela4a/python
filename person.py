class Human:
    # age = 0
    # first_name = ''
    # last_name = ''
    # weight = 80
    age: int
    first_name: str
    last_name: str
    weight: int
    _pasword: str
    __bank_account: str

    counter: int = 0

    def __init__(self, first_name, last_name, age, weight = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.weight = weight
        self._init_password()
        self.__bank_account = '0012kjjfiej'

        Human.counter += 1

    def info(self):
        print(self.first_name, self.age, self.weight)

    def _init_password(self):
        self._password = '123456789'

    def show_bank_account(self):
        print(self.__bank_account[:5] + '******')

john = Human('John', 'Doe', 30)
arture = Human('Arture', 'Doe', 40)

# print(john, arture)
#
# john.age = 30
# john.first_name = 'John'
# john.last_name = 'Doe'
#
# arture.age = 40
# arture.first_name = 'Arture'
# arture.last_name = 'Doe'

# print(john.first_name, john.last_name, john.age, john.weight)
# print(arture.first_name, arture.last_name, arture.age, arture.weight)

john.info()
arture.info()

print(Human.counter)
print(john._password)
print(john.show_bank_account())

# print(john.__bank_account)
# print(john._Human__bank_account)