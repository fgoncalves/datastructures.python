from .stack import Stack

class ListStack(Stack):
    """
    A stack backed up by a list. There's no limit to the stack's capacity
    """

    def __init__(self):
        Stack.__init__(self)
        self.elements = list()
    
    def push(self, element):
        raise NotImplementedError()

    def pop(self):
        raise NotImplementedError()

    def peek(self):
        raise NotImplementedError()

    def is_empty(self):
        raise NotImplementedError()