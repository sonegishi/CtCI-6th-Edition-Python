class Array:
    def __init__(self, capacity):
        self.array = [None for _ in range(capacity)]

    def size(self):
        return len(self.array)

    def equals(self, a2):
        if self.size() != a2.size():
            return False
        return self.array == a2.array

    def sort(self):
        return sorted(self.array)

    def print(self):
        print(self.array)
