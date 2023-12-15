# # Разработайте класс Person, имеющий статический метод is_adult(age), который принимает возраст и возвращает True,
# если возраст больше или равен 18, и False в противном случае.
# class Person:
#     def __init__(self, age):
#         self.age = age
#
#     @staticmethod
#     def is_adult(age):
#         return age >= 18
##########################################################################################################################

# # Создайте класс EmailValidator, в котором определен статический метод is_valid_email(email),
# который проверяет, является ли переданный email адресом формата "user@example.com".
# class EmailValidator:
#     def __init__(self, email):
#         if EmailValidator.is_valid_email(email):
#             self.email = email
#         else:
#             raise ValueError ('неправильный формат адреса!')
#
#     @staticmethod
#     def is_valid_email(email):
#         end = ['@gmail.com', '@ukr.net']
#         return any(email.endswith(elem) for elem in end)
#
# try:
#     email1 = EmailValidator('frantik4446@gmail.1com')
#     print(email1.email)
# except ValueError as e:
#     print(e)
#
# print(EmailValidator.is_valid_email('frantik4446@gmail.com'))
#####################################################################################################33

# # Создайте класс StringUtils, в котором определен статический метод reverse_string(string), который возвращает обратную строку.
# class StringUtils:
#     def __init__(self, string):
#         self.string = string
#
#     @staticmethod
#     def reverse_string(string):
#         if type(string) == str:
#             return "".join(reversed(string))
#         else:
#             raise ValueError('вводится не строка!')
#
#     def __str__(self):
#         return f'{self.string}'
#
# stroka = StringUtils('abcd')
# print(StringUtils.reverse_string(stroka.string))
# print(stroka.__str__())