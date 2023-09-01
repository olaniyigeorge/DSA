'''
Implementation of major Abstract Data Structures
(Stack, Queues, Trees) in Python
'''

class Stack():
    '''
    Implementation of a stack using python lists as a container
    '''
    container = []
    capacity = 0

    def __init__(self, val=[], capacity=10):
        if val:
            for item in val:
                self.container.append(item)
        else:
            self.container = []
        self.capacity = capacity

    def __str__(self):
        return str(self.container)
    
    def pop(self):
        self.container = self.container[:-1]
        return self.container


    def push(self, toBeAdded=None):
        if not toBeAdded:
            raise ValueError("You can't push none to a stack")
        if len(self.container) == self.capacity:
            self.capacity = self.capacity + 1
        self.container.append(toBeAdded)


    def isEmpty(self):
        if len(self.container)<1:
            return True
        return False
    
    def isFull(self):
        if len(self.container) == self.capacity:
            return True
        return False

class Queue():
    '''
    Implementation of a queue using python lists as a container
    '''
    container = []
    capacity = 0

    def __init__(self, val=[], capacity=10):
        if val:
            for item in val:
                self.container.append(item)
        else:
            self.container = []
        self.capacity = capacity

    def __str__(self):
        return str(self.container)
    

    def push(self, toBeAdded=None):
        if not toBeAdded:
            raise ValueError("You can't push none to a stack")
        if len(self.container) == self.capacity:
            self.capacity = self.capacity + 1
        self.container.append(toBeAdded)
    
    
    def pop(self):
        popped = self.container[0]
        self.container = self.container[1:]
        return popped


    def isEmpty(self):
        if len(self.container)<1:
            return True
        return False
    
    def isFull(self):
        if len(self.container) == self.capacity:
            return True
        return False

    def size(self):
        return len(self.container)
