class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    print(s.pop())
