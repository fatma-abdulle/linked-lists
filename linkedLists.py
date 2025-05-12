class Node:
    def __init__(self, data):
        self.data = data  # Data held by the node
        self.next = None  # Reference to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # Initially, the list is empty

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_index(self, index, data):
        new_node = Node(data)
        if index == 0:
            self.insert_at_start(data)
            return
        current = self.head
        count = 0
        while current:
            if count == index - 1:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
            count += 1
        raise IndexError("Index out of range")

    def delete_at_index(self, index):
        if not self.head:
            raise IndexError("List is empty")
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        count = 0
        while current:
            if count == index - 1 and current.next:
                current.next = current.next.next
                return
            current = current.next
            count += 1
        raise IndexError("Index out of range")

    def search(self, value):
        current = self.head
        index = 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print("Linked List:", elements)

# Example usage:git
ll = LinkedList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_start(5)
ll.insert_at_index(1, 15)
ll.display()
print("Index of 20:", ll.search(20))
ll.delete_at_index(2)
ll.display()
