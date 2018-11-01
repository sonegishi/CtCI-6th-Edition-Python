class Queue:
    def __init__(self):
        self.queue = list()

    def enqueue(self, item):
        return self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop(0)

    def peek(self):
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0
