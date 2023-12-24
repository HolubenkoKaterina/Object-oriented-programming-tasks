# Задача: Пользовательский аккаунт
# Реализуйте класс User, представляющий пользователя системы.
# У пользователя должны быть следующие атрибуты:
# username (строка), email (строка) и password (строка).
# При установке username, проверьте, чтобы длина
# была не менее 5 символов, иначе выдайте ошибку:
# "Имя пользователя должно содержать не менее 5 символов."
# При установке email, проверьте, чтобы строка содержала
# символ '@', иначе выдайте ошибку: "Некорректный адрес электронной почты."
# При установке password, проверьте, чтобы длина была
# не менее 8 символов, иначе выдайте ошибку:\
#     "Пароль должен содержать не менее 8 символов."
# Реализуйте эти проверки с использованием сеттеров.

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __setattr__(self, key, value):
        if key == 'username':
            if not isinstance(value, str) or len(value) < 5:
                raise ValueError("Имя пользователя должно содержать не менее 5 символов.")
        elif key == 'email':
            if not isinstance(value, str) or '@' not in value:
                raise ValueError("Некорректный адрес электронной почты.")
        elif key == 'password':
            if not isinstance(value, str) or len(value) < 8:
                raise ValueError("Пароль должен содержать не менее 8 символов.")

        object.__setattr__(self, key, value)

    def __str__(self):
        return f'{self.username} {self.email} {self.password}'

# user1 = User('katya', 'franttytttt@gmail.com', '5587pjgyv')
# print(user1)
# print(user1.__dict__)
user2 = User('katya', 'frantttttttgmail.com', '5587pjgyv')
print(user2.__dict__)
