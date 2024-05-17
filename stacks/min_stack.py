# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

class MinStack(object):
    def __init__(self):
        self.min_stack = []
        self.main_stack = []

    def push(self, value):
        self.main_stack.push(value)
        if len(self.min_stack) == 0:
            self.min_stack.append(value)
        elif self.min_stack[-1] >= value:
            self.min_stack.append(value)

    def pop(self):
        value_popped = self.main_stack.pop()
        if value_popped == self.min_stack[-1]:
            self.min_stack.pop()
    
    def top(self):
        if len(self.main_stack) == 0:
            return None
        return self.main_stack[-1]
    
    def get_min(self):
        if len(self.main_stack) == 0:
            return None
        return self.min_stack[-1]


