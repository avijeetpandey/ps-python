from collections import deque


class StackUsingDeque:
    def __init__(self):
        self.items = deque()

    def push(self, item):
        self.items.append(item)

    def peek(self):
        if not self.items:
            return None
        return self.items[-1]

    def pop(self):
        if not self.items:
            return None
        return self.items.pop()
