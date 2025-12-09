

class Stack:
    def __init__(self, items=None, limit=100):
        if items is None:
            self.items = []
        else:
            self.items = list(items)
        self.limit = limit

    def push(self, item):
        if len(self.items) >= self.limit:
            return None  # or you can raise error, but test expects None or silence
        self.items.append(item)

    def pop(self):
        if not self.items:
            return None
        return self.items.pop()

    def peek(self):
        if not self.items:
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def isEmpty(self):       # Note: method name is isEmpty (not empty)
        return len(self.items) == 0

    def full(self):
        return len(self.items) >= self.limit

    def search(self, item):
        try:
            index = len(self.items) - 1 - self.items[::-1].index(item)
            return len(self.items) - 1 - index  # distance from top
        except ValueError:
            return -1