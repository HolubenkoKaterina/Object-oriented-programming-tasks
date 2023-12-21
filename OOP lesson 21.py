# Задача: Учет сотрудников в компании
# Создайте класс Employee для представления информации
# о сотруднике компании. Сотрудник должен иметь следующие свойства:
# name (имя сотрудника),
# position (должность),
# salary (заработная плата).
# Реализуйте методы в классе Employee:
# get_details(): возвращает строку с подробной
# информацией о сотруднике в формате "Имя: [имя],
# Должность: [должность], Заработная плата: [заработная плата]".
# Создайте класс Company, представляющий компанию.
# Компания должна хранить список сотрудников.
# Реализуйте методы в классе Company:
# hire_employee(employee): добавляет сотрудника в список компании.
# fire_employee(employee): удаляет сотрудника из списка компании.
# get_employee_details(): возвращает список строк с
# информацией о каждом сотруднике.
# Создайте несколько объектов Employee и объект Company.
# Наймите и увольте несколько сотрудников, а затем
# выведите информацию о всех сотрудниках в компании.

class Employee:
    def __init__(self, name, lastname, position, salary):
        self._name = name.title()
        self._lastname = lastname.title()
        self._position = position
        self._salary = salary

    def __str__(self):
        return f'Имя: {self._name} Фамилия {self._lastname}\nДолжность: {self._position}\nЗаработная плата: {self._salary}'

    @property
    def lastname(self):
        return self._lastname

class Company:
    def __init__(self):
        self.__emp_list = []

    @property
    def employees(self):
        return self.__emp_list

    def get_employee_by_lastname(self, lastname_find):
        lastname_find_lower = lastname_find.lower()
        lastname_find_list = []
        for employee in self.__emp_list:
            if lastname_find_lower in employee.lastname.lower():
                lastname_find_list.append(employee)
        if not lastname_find_list:
            return None
        else:
            return lastname_find_list

    def hire_employee(self, employee):
        if employee not in self.__emp_list:
            self.__emp_list.append(employee)
        else:
            raise ValueError('такой сотрудник в компании оформлен!')

    def fire_employee(self, employee):
        if employee in self.__emp_list:
            self.__emp_list.remove(employee)
        else:
            raise ValueError('такой сотрудник в компании не оформлен!')

    def get_employee_details(self, e):
        return self.__emp_list

    def get_employees(self):
        return self.__emp_list

book_supermarket = Company()
emp1 = Employee('Сергей', "Бачаров", "менеджер", 20000)
emp2 = Employee('Федоров', "Евгений", "директор", 50000)
emp3 = Employee('Федорова', "Алла", "ком.директор", 45000)
book_supermarket.hire_employee(emp1)
book_supermarket.hire_employee(emp2)
book_supermarket.hire_employee(emp3)

print(book_supermarket.get_employee_by_lastname('Фе'))
