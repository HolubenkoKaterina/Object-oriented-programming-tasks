# Разработайте класс Person,
# который принимает имя и фамилию, но возвращает только уникальные объекты для разных людей с одинаковыми именами и фамилиями.

class Person:
    _instance = {}

    def __new__(cls, *args, **kwargs):
        name, surname = args
        if (name, surname) not in cls._instance:
            new_person = super().__new__(cls)
            cls._instance[(name, surname)] = new_person
        return cls._instance[(name, surname)]

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

person1 = Person('vasya', 'pupkin')
person2 = Person('lili', 'kiki')
person3 = Person('lili', 'kiki')

print(person2 is person3)
print(person1 is person2)
