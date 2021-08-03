class node:
    def _init_(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DoublyLinkedList:
        def _init_(self):
            self.head=None


        def add_node_in_beggining(self, data):
            new_node = node(data)
            new_node.next = self.head
            if self.head is not None:
                self.head.prev = new_node
            self.head = new_node

        def add_at_particular_value(self, data, position):
            new_node= node(data)
            if self.head = None:
                self.add_in_beggining(data)
            else:
                temp = self.head
                count_val = 1
                while (temp):
                    if position == count_val:
                        temp_node = temp.next
                        new_node.next = temp_node
                        temp.next = new_node
                        new_node.next = prev_node.next
                        prev_node.next = new_node

                    count_val +=1
                    temp = temp.next
            return print (DoublyLinkedList)

