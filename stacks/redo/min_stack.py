class MinStack(object):

    def __init__(self):
        self.stack = []
        self.lowest_tracker = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        
        self.stack.append(val)
        if not self.lowest_tracker:
            self.lowest_tracker.append(val)
        elif val <= self.getMin():
            self.lowest_tracker.append(val)

    def pop(self):
        """
        :rtype: None
        """
        if self.stack.pop() == self.getMin():
            self.lowest_tracker.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.lowest_tracker[-1]
    


obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())