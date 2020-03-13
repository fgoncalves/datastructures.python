class Stack:
    """
    A datastructure that implements a last in first out strategy.
    """

    def push(self, element):
        """
        Add an element to the stack

        :param element: The element to add
        """
        raise NotImplementedError()

    def pop(self):
        """
        Remove the last added element

        :return: The element that was removed
        """
        raise NotImplementedError()

    def peek(self):
        """
        Get the last element added to the stack but do not remove it
        
        :return: The last added element
        """
        raise NotImplementedError()

    def is_empty(self):
        """
        Check if the stack is empty

        :return: True if the stack is empty. False otherwise
        """
        raise NotImplementedError()