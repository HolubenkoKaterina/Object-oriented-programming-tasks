# class ObjList:
#     def __init__(self, data):
#         self.__data = data
#         self.__next = None
#         self.__prev = None
#
#     @property
#     def data(self):
#         return self.__data
#
#     @property
#     def next(self):
#         return self.__next
#
#     @next.setter
#     def next(self, next):
#         self.__next = next
#
#     @property
#     def prev(self):
#         return self.__prev
#
#     @prev.setter
#     def prev(self, prev):
#         self.__prev = prev
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None  # ObjList
#         self.tail = None  # ObjList
#
#     def add_obj(self, obj):
#         if not self.head:
#             self.head = obj
#             self.tail = obj
#         else:
#             obj.prev = self.tail
#             self.tail.next = obj
#             self.tail = obj
#
#     def pop_obj(self):
#         if not self.head:
#             return None
#
#         removed_obj = self.tail  # уже хвост
#         if self.head == self.tail:
#             self.head = None
#             self.tail = None
#         else:
#             prev_obj = removed_obj.prev  # предыдущий элемент, который станет хвостом
#             prev_obj.next = None
#             self.tail = prev_obj
#         return removed_obj
#
#     def get_data(self):
#         data_list = []
#         current_obj = self.head  # ObjList
#         while current_obj:
#             data_list.append(current_obj.data)
#             current_obj = current_obj.next
#         return data_list
#
#
# linkedlist = LinkedList()
# linkedlist.add_obj(ObjList(1))
# linkedlist.add_obj(ObjList(7))
# linkedlist.add_obj(ObjList(101))
#
# print(linkedlist.get_data())
# print("remove data:", linkedlist.pop_obj().data)
# print(linkedlist.get_data())