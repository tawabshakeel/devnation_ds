class node:
    def __init__(self, data):
        self.data = data
        self.next = none


class CircularLinkedList:
    def __init__(self):
        self.head = none
    def print_list(self):
        temp = self.head
        if self.head is not none:
            while(True):
                print (temp.data)
                temp = temp.next
                if temp == self.head:
                    break
    def add_at_particular_position(self, new_data, position):
        new_node = node(new_data)
        if self.head is none:
            self.head = new_node
            new_node.next == self.head
        else:
            temp = self.head
            count_val = 1
            while (temp):
                if position == count_val:
                    temp_node = temp.next
                    new_node.next = temp_node
                    temp.next = new_node
                    break
                temp = temp.next
                count_val +=1

    def add_at_begining(self, new_data):
        new_node = node(new_data)
        if self.head is none:
            self.head = new_node
            new_node.next == self.head
        else:
            temp = self.head
            count_val = 0
            while (temp):
                if position == count_val:
                    new_node.next= temp
                    temp = new_node
                    temp.next = new_node.next
                    break
                temp = temp.next
                count_val +=1
    def add_at_end (self, new_data):
        new_node = node(new_data)
        if self.head is none:
            self.head = new_node
            new_node.next == self.head
        else:
            temp = self.head
            count_val =

