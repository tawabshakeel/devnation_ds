class Stack:

    def __init__(self, items=0):
        self.items = []

    def push(self, data):
        return self.items.insert(0, data)

    def pop(self, x=0):
        if self.isEmpty():
            pass
        else:
            return self.items.pop(x)

    def peak(self):
        if self.isEmpty():
            pass
        else:
            return self.items[0]

    def print_stack(self):
        if self.isEmpty():
            pass
        else:
            return self.items

    def size(self):
        if self.isEmpty():
            pass
        else:
            return len(self.items)

    def isEmpty(self):
        if len(self.items) == 0:
            return ("Empty stack")