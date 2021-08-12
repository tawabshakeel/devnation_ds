class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def peek (self):
        if self.items != 0:
            return self.items [-1]
        else:
            pass


    def dequeue (self):
        return self.items.pop(0)

    def size (self):
        return len (self.items)

    def dequeue_without_using_insert(self):
        self.items.append(0, items)


    def print_queue(self):
        for i in self.items:
            print (i)