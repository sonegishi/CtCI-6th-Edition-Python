from Array import Array


class ArrayStacks:
    def __init__(self, capacity):
        self.stacks = Array(capacity)
        self.indexes = [i for i in range(self.stacks.size()) if i % int(self.stacks.size()/3) == 0]

    def pop(self, index):
        pass

    def push(self, index, item):
        if index == 0:
            pass
        elif index == 1:
            pass
        elif index == 2:
            self.stacks[33] = item
        else:
            return

    def peak(self):
        if self.is_empty():
            return None
        else:
            return

    def size(self):
        pass

    def is_empty(self):
        pass


if __name__ == '__main__':
    stacks = ArrayStacks(100)
    stacks.push(2, 50)
    print(stacks.stacks)
