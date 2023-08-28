class Stack:

    class Node:
        def __init__(self, item, _next=None):
            self.item = item
            self.next = _next

    def __init__(self):
        self.size = 0
        self.top = None

    def push(self, item):
        old_top = self.top
        self.top = self.Node(item, old_top)
        self.size += 1

    def pop(self):
        if self.top:
            item = self.top.item
            self.top = self.top.next

            self.size -= 1
            return item

        return None

    def get_top(self):
        if self.top is not None:
            return self.top.item

        return None

    @property
    def is_empty(self):
        return self.size == 0

    def size(self):
        return self.size
