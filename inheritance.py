class Person:
    _first_name: str
    _last_name: str

    def __init__(self, first_name: str, last_name: str):
        self._first_name = first_name
        self._last_name = last_name

    def Fullname(self):
        return f'{self._first_name} {self._last_name}'

class User(Person):
    login: str
    password: str

    def __init__(self, first_name: str, last_name: str, login: str):
        super().__init__(first_name, last_name)
        self.login = login

    def log_in(self):
        print(self.Fullname())

class InfoPtinter:
    def info (self, class_object):
        if isinstance(class_object, User):
            print('Its a person')
        elif isinstance(class_object, Person):
            print('Its a user')
        else:
            print('unknown')


john = User('John', 'Doe', 'h777')
artur = Person('Artur', 'Doe')

john.log_in()

printer = InfoPtinter()
printer.info(artur)
printer.info(john)
printer.info([])

