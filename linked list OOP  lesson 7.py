# Связанный список (Linked List) - это структура данных, состоящая из узлов,
# каждый из которых содержит какое-то значение и ссылку (или указатель) на следующий узел в списке.
# Основные типы связанных списков:
# Однонаправленный связанный список (Singly Linked List):
#    - Каждый узел содержит значение и указатель на следующий узел.
#    - У последнего узла указатель на следующий узел равен `None`.
# Преимущества связанных списков:
# - Динамичность: размер связанного списка может изменяться во время выполнения программы.
# - Вставка и удаление элементов: эти операции выполняются быстрее, чем в массивах, так как не требуется перемещать элементы.
# Недостатки:
# - Отсутствие прямого доступа к элементам по индексу. Для доступа к элементу необходимо пройти все предыдущие узлы.

class Node:
    def __init__(self, elem=None):
        self.elem = elem
        self.next_elem = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add_element(self, elem):
        new_node = Node(elem)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_elem is not None:
                current_node = current_node.next_elem
            current_node.next_elem = new_node

    def display(self):
        elements = []
        current_node = self.head
        while current_node is not None:
            elements.append(current_node.elem)
            current_node = current_node.next_elem
        return elements


linked_list = LinkedList()
linked_list.add_element(10)
linked_list.add_element(20)
linked_list.add_element(30)

print(linked_list.display())
