# 29. Найдите наиболее часто встречающийся элемент в словаре.
# my_dict = {1: 2, 2: 2, 3: 2, 4: 2, 5: 2}
# max_count = max(my_dict.values())
# most_common_elements = [key for key, val in my_dict.items() if val == max_count]
# print("Наиболее часто встречающиеся элементы:", most_common_elements)

# 30. Удалите элемент с наименьшим значением в словаре.
# my_dict = {1: 2, 2: 2, 3: 2, 4: 2, 5: 12}
# min_val = min(my_dict.values())
# my_dict_new = {key: val for key, val in my_dict.items() if val != min_val}
# print(my_dict_new)


# 31. Создайте словарь, в котором значения являются словарями.
# 32. Получите значение из вложенного словаря по нескольким ключам.
# my_dict = {
#     'dict1': {'a': 1, 'b': 2, 'c': 3},
#     'dict2': {'x': 10, 'y': 20, 'z': 30},
#     'dict3': {'apple': 'red', 'banana': 'yellow', 'grape': 'purple'}
# }
# list_out = []
# for key, val in my_dict.items():
#     if 'apple' in val:
#         list_out.append(val['apple'])
# print(list_out)

# 33. Создайте словарь, содержащий информацию о студентах (имя, возраст, оценки и т. д.).
# 34. Найдите средний возраст студентов в словаре из предыдущей задачи.
# 35. Удалите студента из словаря на основе его имени.
# 36. Обновите оценку студента в словаре.
# students = {
#     'student1': {
#         'name': 'Иванов Иван',
#         'age': 20,
#         'grades': [4, 5, 3, 4]
#     },
#     'student2': {
#         'name': 'Петров Петр',
#         'age': 19,
#         'grades': [5, 5, 4, 5]
#     },
#     'student3': {
#         'name': 'Сидоров Сидор',
#         'age': 21,
#         'grades': [3, 4, 3, 3]
#     }
# }
# def aver_age_students(some_dict: dict):
#     list_age = []
#
#     summa = 0
#     for student, val in some_dict.items():
#         age = val['age']
#         grade = val['grades']
#         name_student = val['name']
#         list_age.append(age)
#     for elem in list_age:
#         summa += elem
#         aver_age = summa / len(list_age)
#
#     return (f'средний возраст студентов {aver_age}')
# print(aver_age_students(students))

# def del_student(some_dict: dict, st_name):
#     new_dict = {}
#     for student, val in some_dict.items():
#         name_student = val['name']
#         if name_student != st_name:
#             new_dict[student] = val
#     return new_dict
# print(del_student(students, st_name='Сидоров Сидор'))

