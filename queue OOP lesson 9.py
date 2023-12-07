# Класс данных «очередь» представляет собой структуру данных, в которой элементы обрабатываются
# по принципу «первым — первым обслужен» .
# Это означает, что элементы, добавленные в очередь раньше, будут извлечены раньше всех остальных.
# Очереди, используемые в алгоритмах обхода графов (например, поиск в настройках).
# Очереди часто применяются в сетевом программировании и многопоточных приложениях для решения задач управления.
class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if not self.isempty():
            self.queue.pop(0)
        else:
            raise IndexError("Очередь пустая")

    def peek(self):
        if not self.isempty():
            return self.queue[-1]
        else:
            raise IndexError("Очередь пустая")

    def isempty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

queue1 = Queue()
queue1.push(1)
queue1.push(2)
queue1.push(3)
print(queue1.queue)
queue1.pop()
print(queue1.queue)
print(queue1.size())
