# # Разработайте класс Employee, который представляет информацию о сотруднике, и класс Company,
# который содержит список сотрудников.
# Используйте статический метод find_employee_by_id(employee_id), чтобы найти сотрудника по его идентификатору внутри класса Company.
# class Employee:
#     __EMPLOYEE_base = {}
#
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
#         Employee.__EMPLOYEE_base[id] = self
#
#     @staticmethod
#     def find_employee_by_id(employee_id):
#         return Employee.__EMPLOYEE_base.get(employee_id)
#
#
# class Company:
#     def __init__(self):
#         self.employees = []
#
#     def add_employee(self, employee):
#         self.employees.append(employee)
#
#     def find_employee_by_id(self, employee_id):
#         for employee in self.employees:
#             if employee.id == employee_id:
#                 return employee
#         return None
#
#
# # Пример использования:
# company = Company()
# emp1 = Employee(125, 'Sokolov Ivan')
# emp2 = Employee(135, 'Sokolova Ivanna')
#
# company.add_employee(emp1)
# company.add_employee(emp2)
#
# found_employee = company.find_employee_by_id(125)
# if found_employee:
#     print(f"Found employee: {found_employee.name}")
# else:
#     print("Employee not found.")
###############################################################################################################3

# # Напишите класс AuthorizationManager, который управляет правами доступа.
# Определите статические методы grant_permission и revoke_permission,
# а также классовый метод perform_permission_operation, который позволяет выбирать и выполнять операции с правами доступа.
# class AuthorizationManager:
#     __allowed_actions = ["read", "write"]
#     __doing_action = None
#
#     def __init__(self, name_user):
#         self.name_user = name_user
#
#     @classmethod
#     def grant_permission(cls, name_user, action):
#         if action in cls.__allowed_actions:
#             cls.__doing_action = action
#         else:
#             raise ValueError(f"Invalid action: {action}")
#
#     @classmethod
#     def revoke_permission(cls, name_user):
#         if cls.__doing_action is not None:
#             cls.__doing_action = None
#         else:
#             raise ValueError("No permission to revoke")
#
#     @classmethod
#     def get_doing_action(cls):
#         return cls.__doing_action
#
# person1 = AuthorizationManager('ivan')
# AuthorizationManager.grant_permission('ivan', 'read')
# print(AuthorizationManager.get_doing_action())
# AuthorizationManager.revoke_permission('ivan')
# print(AuthorizationManager.get_doing_action())
# ###################################################################################################################

# Объявите класс для мессенджера с именем Viber. В этом классе должны быть следующие методы:
# add_message(msg) - добавление нового сообщения в список сообщений;
# remove_message(msg) - удаление сообщения из списка;
# set_like(msg) - поставить/убрать лайк для сообщения msg (т.е. изменить атрибут fl_like объекта msg: если лайка нет то он ставится, если уже есть, то убирается);
# show_last_message(число) - отображение последних сообщений;
# total_messages() - возвращает общее число сообщений.
# Эти методы предполагается использовать следующим образом (эти строчки в программе не писать):

# msg = Message("Всем привет!")
# Viber.add_message(msg)
# Viber.add_message(Message("Это курс по Python ООП."))
# Viber.add_message(Message("Что вы о нем думаете?"))
# Viber.set_like(msg)
# Viber.remove_message(msg)
#
# Класс Message (необходимо также объявить) позволяет создавать объекты-сообщения со следующим набором локальных свойств:
#
# text - текст сообщения (строка);
# fl_like - поставлен или не поставлен лайк у сообщения (булево значение True - если лайк есть и False - в противном случае, изначально False);
# class Viber:
#     __SMS_lists = []
#
#     @classmethod
#     def add_message(cls, msg):
#         cls.__SMS_lists.append(msg)
#
#     @classmethod
#     def remove_message(cls, msg):
#         if msg in cls.__SMS_lists:
#             cls.__SMS_lists.remove(msg)
#         else:
#             print('Сообщений нет')
#
#     @classmethod
#     def total_messages(cls):
#         return len(cls.__SMS_lists)
#
#     @classmethod
#     def show_last_message(cls, num):
#         if len(cls.__SMS_lists) == 0:
#             print('Список сообщений пуст')
#         elif len(cls.__SMS_lists) >= num:
#             print([str(msg) for msg in cls.__SMS_lists[-num:]])
#         else:
#             print([str(msg) for msg in cls.__SMS_lists])
#
#     @classmethod
#     def set_like(cls, msg):
#         if msg.fl_like is None:
#             msg.fl_like = True
#         else:
#             msg.fl_like = not msg.fl_like
#
#
# class Message:
#     def __init__(self, text, fl_like=False):
#         self.text = text
#         self.fl_like = fl_like
#
#     def __str__(self):
#         return f'{self.text}'
#
# # Пример использования
# msg1 = Message("Всем привет!")
# Viber.add_message(msg1)
# Viber.add_message(Message("Это курс по Python ООП."))
# Viber.add_message(Message("Что вы о нем думаете?"))
# Viber.set_like(msg1)
# Viber.show_last_message(2)
# Viber.remove_message(msg1)
# Viber.show_last_message(2)















# Объявите класс AppStore - интернет-магазин приложений для устройств под iOS. В этом классе должны быть реализованы следующие методы:
#
# add_application(self, app) - добавление нового приложения app в магазин;
# remove_application(self, app) - удаление приложения app из магазина;
# block_application(self, app) - блокировка приложения app (устанавливает локальное свойство blocked объекта app в значение True);
# total_apps(self) - возвращает общее число приложений в магазине.
#
# Класс AppStore предполагается использовать следующим образом (эти строчки в программе не писать):
#
# store = AppStore()
# app_youtube = Application("Youtube")
# store.add_application(app_youtube)
# store.remove_application(app_youtube)
#
#
# Здесь Application - класс, описывающий добавляемое приложение с указанным именем. Каждый объект класса Application должен содержать локальные свойства:
#
# name - наименование приложения (строка);
# blocked - булево значение (True - приложение заблокировано; False - не заблокировано, изначально False).
#
# Как хранить список приложений в объектах класса AppStore решите сами.