# Задача: Счетчик с ограничением без наследования
# Создайте класс LimitedCounter, который будет реализовывать
# функциональность счетчика с ограничением максимального значения.
# Класс должен иметь атрибуты count (текущее значение счетчика)
# и limit (максимальное значение счетчика).
# При установке ограничения, если счетчик превышает это
# значение, он должен автоматически сбрасываться на ноль.

# class LimitedCounter:
#     def __init__(self, limit, count=0):
#         self.count = count
#         self.limit = limit
#
#     def __call__(self, *args, **kwargs):
#         if self.count > self.limit:
#             self.count = 0
#         return self.count
#
#     def counter_increment(self):
#         if self.count > self.limit:
#             self.count = 0
#         else:
#             self.count += 1
#
# # Создаем экземпляр LimitedCounter с лимитом 1
# counter = LimitedCounter(1)
# # Печатаем текущее значение счетчика (должно быть 0)
# print(counter())  # Вывод: 0
# # Увеличиваем счетчик на 3
# counter.counter_increment()
# # Печатаем текущее значение счетчика (должно быть 0, так как счетчик превысил лимит)
# print(counter())  # Вывод: 0
