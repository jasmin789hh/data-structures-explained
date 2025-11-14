class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.items:
            return self.items.pop(0)
        return None

if __name__ == "__main__":
    q = Queue()
    q.enqueue(5)
    q.enqueue(15)
    print(q.dequeue())
