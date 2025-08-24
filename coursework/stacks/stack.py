# implement stack in python using Linkedlist
class Stack:
    def __init__(self):
        self.items = []
    
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
    
"""
Though implementing stacks using list is a native way of implementing stack in python but it has 
one drawback i.e it is not memory efficient when it comes to storing larger datasets,
as finding a continuous memory chunk to store data can be challenging.
"""
