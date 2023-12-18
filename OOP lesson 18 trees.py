# # class TreeObj:
# #     def __init__(self, index, data=None):
# #         self.__index = index
# #         self.__left = None
# #         self.__right = None
# #         self.__data = data
# #
# #     @property
# #     def data(self):
# #         return self.__data
# #
# #     @property
# #     def left(self):
# #         return self.__left
# #
# #     @left.setter
# #     def left(self, left):
# #         self.__left = left
# #
# #     @property
# #     def right(self):
# #         return self.__right
# #
# #     @right.setter
# #     def right(self, right):
# #         self.__right = right
# #
# #     @property
# #     def index(self):
# #         return self.__index
# #
# #
# # class Tree:
# #     @staticmethod
# #     def add(obj, node=None, left=True):
# #         if node is None:
# #             return obj
# #         if left:
# #             node.left = obj
# #         else:
# #             node.right = obj
# #         return obj
# #
# #     @staticmethod
# #     def predict(root, routes):
# #         node = root
# #         while node.left is not None and node.right is not None:
# #             if routes[node.index] == 1:
# #                 node = node.left
# #             else:
# #                 node = node.right
# #         return node.data
# #
# #
# # root = Tree.add(TreeObj(0))
# # branch1 = Tree.add(TreeObj(1), root)
# # branch2 = Tree.add(TreeObj(2), root, False)
# # Tree.add(TreeObj(-1, "будет программистом"), branch1)
# # Tree.add(TreeObj(-1, "будет кодером"), branch1, False)
# # Tree.add(TreeObj(-1, "не все потярено"), branch2)
# # Tree.add(TreeObj(-1, "безнадежен"), branch2, False)
# #
# # routes = [1, 1, 0]
# #
# # print(Tree.predict(root, routes))
#
# # root = Tree.add(TreeObj(0, "Любит Python"))
# # branch = Tree.add(TreeObj(0, "Любит кунг-фу Панда"), root)
#
