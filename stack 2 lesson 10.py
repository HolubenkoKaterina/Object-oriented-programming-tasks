
class Unknown:
    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.append(item)

    def pop(self):
        if self.list:
            return self.list.pop()
        else:
            raise IndexError("list пустой")

    def get_last_element(self):
        if self.list:
            return self.list[-1]
        else:
            raise IndexError("list пустой")

    def isempty(self):
        return len(self.list) == 0

    def size(self):
        return len(self.list)

    def get_data(self):
        return self.list

unknown1 = Unknown()
print(unknown1.size())
unknown1.push(12)
unknown1.push(2)
unknown1.push(13)
unknown1.push(45)
unknown1.push(28)
print(unknown1.size())
print(unknown1.get_data())
unknown1.pop()
print(unknown1.get_data())
print(unknown1.get_last_element())





