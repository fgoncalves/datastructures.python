from array import array

from .stack import Stack


class ArrayStack(Stack):
    """
    A stack backed up by the `array module <https://docs.python.org/3/library/array.html>`_

    This stack has a limit of capacity and will raise an exception if the limit is exceeded.

    :param typecode: The type code to hold in the backing array
    :param capacity: The capacity for the stack. Defaults to 10.
    """

    def __init__(self, typecode, capacity=10):
        Stack.__init__(self)
        self.elements = array(typecode)
        self.capacity = capacity

    def push(self, element):
        """
        Add an element to the stack.

        :param element: The element to add

        :raise MemoryError: When the stack is full
        """
        raise NotImplementedError()

    def pop(self):
        raise NotImplementedError()

    def peek(self):
        raise NotImplementedError()

    def is_empty(self):
        raise NotImplementedError()