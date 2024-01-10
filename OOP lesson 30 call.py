# Хорошо, давайте создадим класс Counter, который будет
# представлять счетчик. Класс должен иметь атрибут count,
# который будет отслеживать текущее значение счетчика.
# Также, у этого класса должен быть метод increment,
# который увеличивает значение счетчика на 1,
# и метод reset, который сбрасывает счетчик в ноль.
# Ваша задача - добавить метод __call__ к этому классу так,
# чтобы экземпляр класса Counter можно было вызывать
# как функцию для увеличения значения счетчика на заданную величину.
#
# class Counter:
#     def __init__(self, count=0):
#         self.count = count
#
#
#     def counter_increment(self):
#         self.count += 1
#
#     def reset(self):
#         self.count = 0
#
#     def __call__(self, *args, **kwargs):
#         self.count += args[0]
#         return self.count
#
# counter = Counter()
# print(counter.count)  # Вывод: 0
# counter.counter_increment()
# print(counter.count)  # Вывод: 1
# counter(5)  # Эквивалент вызова counter.__call__(5)
# print(counter.count)  # Вывод: 6
