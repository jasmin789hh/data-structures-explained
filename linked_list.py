class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

if __name__ == "__main__":
    ll = LinkedList()
    ll.add(3)
    ll.add(7)
