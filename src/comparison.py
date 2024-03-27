from .stack import Stack


class Comparison:
    """
    This class contains methods for comparison operations
    """

    def greater(self, stack: Stack) -> None:
        """
        This method pops two values from the stack and pushes 1 if the first value is greater than the second, else 0
        :param stack: Stack object
        :return: None
        """
        try:
            value = stack.pop() < stack.pop()
            stack.push(int(value))
        except IndexError:
            raise IndexError("Stack is empty")

    def less(self, stack: Stack) -> None:
        """
        This method pops two values from the stack and pushes 1 if the first value is less than the second, else 0
        :param stack: Stack object
        :return: None
        """
        try:
            value = stack.pop() > stack.pop()
            stack.push(int(value))
        except IndexError:
            raise IndexError("Stack is empty")

    def equal(self, stack: Stack) -> None:
        """
        This method pops two values from the stack and pushes 1 if the first value is equal to the second, else 0
        :param stack: Stack object
        :return: None
        """
        try:
            value = stack.pop() == stack.pop()
            stack.push(int(value))
        except IndexError:
            raise IndexError("Stack is empty")

    def isnil(self, stack: Stack) -> None:
        """
        This method pops a value from the stack and pushes 1 if the value is 0, else 0
        :param stack: Stack object
        :return: None
        """
        try:
            value = stack.pop() == 0
            stack.push(int(value))
        except IndexError:
            raise IndexError("Stack is empty")

    def ispos(self, stack: Stack) -> None:
        """
        This method pops a value from the stack and pushes 1 if the value is positive, else 0
        :param stack: Stack object
        :return: None
        """
        try:
            value = stack.pop() > 0
            stack.push(int(value))
        except IndexError:
            raise IndexError("Stack is empty")

    def isneg(self, stack: Stack) -> None:
        """
        This method pops a value from the stack and pushes 1 if the value is negative, else 0
        :param stack: Stack object
        :return: None
        """
        try:
            value = stack.pop() < 0
            stack.push(int(value))
        except IndexError:
            raise IndexError("Stack is empty")

    def cmp(self, stack: Stack) -> None:
        """
        This method pops two values from the stack and pushes 1 if the first value is greater than the second, 0 if equal, else -1
        :param stack: Stack object
        :return: None
        """
        try:
            first_value = stack.pop()
            second_value = stack.pop()
            value = int(first_value > second_value) - \
                (first_value < second_value)
            stack.push(int(value))
        except IndexError:
            raise IndexError("Stack is empty")
