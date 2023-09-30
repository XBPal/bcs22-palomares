class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def sortList(self):
        current = self.head
        index = None

        if(self.head == None):
            return;
        else:
            while current:
                index = current.next

                while(index != None):
                    if(current.data < index.data):
                        temp = current.data
                        current.data = index.data
                        index.data = temp;
                    index = index.next
                current = current.next

    def display(self):
        current = self.head
        while(current != None):
            print(current.data, end = " -> ")
            current = current.next
        print("None")


#input values
input_values = [6, 3, 4, 2, 1]
sList = LinkedList()
for value in input_values:
    sList.insert(value)

sList.sortList()
#display the linked list
sList.display()