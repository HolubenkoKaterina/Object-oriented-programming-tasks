class Person:
    def __init__(self, name, age):
        self._name = name.title()
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    def __setattr__(self, key, value):
        if key == '_age':
            if not isinstance(value, int) or not (0 <= value < 150):
                raise ValueError('некорректно указываете возраст!')
        if key == '_name':
            if not isinstance(value, str) or  len(value) < 1:
                raise ValueError('некорректно указываете имя!')
        object.__setattr__(self, key, value)

    def __str__(self):
        return f'{self.name} {self.age}'


class Persons:
    def __init__(self):
        self._list_persons = []

    def add_person(self, person):
        self._list_persons.append(person)

    @property
    def list_person(self):
        return self._list_persons

    def __str__(self):
        return ', '.join(str(person) for person in self._list_persons)
    

# создаем экземпляр класса Person
person1 = Person('alla', 56)
person2 = Person('alice', 25)

# создаем экземпляр класса Persons
persons_list = Persons()
persons_list.add_person(person1)
persons_list.add_person(person2)
print(persons_list)
print([str(person) for person in persons_list.list_person])
