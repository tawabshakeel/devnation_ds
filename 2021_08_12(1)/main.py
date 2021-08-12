class Queue:
    # constructors
    def __init__(self):
        self.items = []
# fun to add item at start
    def enqueue(self, item):
        return self.items.insert(0, item)

# function to remove element from last
    def dequeue(self):
        if self.size() > 0:
            return self.items.pop(-1)

    # function to return last item
    def peak(self):
        if self.size() > 0:
            return self.items[-1]

# function to print entire queue
    def print_queue(self):
        if self.size() > 0:
            for i in self.items:
                print(i)

    # function to return length of queue
    def size(self):
        return len(self.items)

    # function to add element without using insert
    def enqueue_without_using_insert(self, item):
        final_list = []
        final_list.insert(0, item)
        for i in self.items:
            final_list.append(i)
        self.items = final_list


# obj creation of class Queue
obj1 = Queue()
obj1.enqueue(1)
obj1.enqueue(2)
obj1.enqueue(3)
obj1.enqueue(4)
obj1.dequeue()
obj1.peak()
obj1.size()
obj1.enqueue_without_using_insert(5)
obj1.print_queue()



