class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        return self.__items.pop()

    def get_stack(self):
        return self.__items

    def is_empty(self):
        return self.__items == []

    def peek(self):
        if not self.is_empty():
            return self.__items[-1]
        else:
            return False

# s = Stack()
# s.push("A")
# s.push("B")
# s.push("C")
# print(s.get_stack())
# s.pop()
# print(s.get_stack())
# s.pop()
# print(s.get_stack())
# print(s.is_empty())
# print(s.peek())