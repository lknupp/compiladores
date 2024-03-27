from .stack import Stack


class Logical:
    """
    This class contains methods for logical operations
    """

    def and_(self, stack: Stack) -> None:
        """
        This method pops two values from the stack and pushes their logical AND back to the stack
        :param stack: Stack object
        :return: None
        """
        try:
            value = stack.pop() and stack.pop()
            stack.push(int(value))
        except IndexError:
            raise IndexError("Stack is empty")

    def or_(self, stack: Stack) -> None:
        """
        This method pops two values from the stack and pushes their logical OR back to the stack
        :param stack: Stack object
        :return: None
        """
        try:
            value = stack.pop() or stack.pop()
            stack.push(int(value))
        except IndexError:
            raise IndexError("Stack is empty")

    def not_(self, stack: Stack) -> None:
        """
        This method pops a value from the stack and pushes its logical NOT back to the stack
        :param stack: Stack object
        :return: None
        """
        try:
            value = not stack.pop()
            stack.push(value)
        except IndexError:
            raise IndexError("Stack is empty")

    def xor(self, stack: Stack) -> None:
        """
        This method pops two values from the stack and pushes their XOR back to the stack
        :param stack: Stack object
        :return: None
        """
        try:
            value = stack.pop() ^ stack.pop()
            stack.push(value)
        except IndexError:
            raise IndexError("Stack is empty")

    def nand(self, stack: Stack) -> None:
        """
        This method pops two values from the stack and pushes their NAND back to the stack
        :param stack: Stack object
        :return: None
        """
        try:
            value = not (stack.pop() and stack.pop())
            stack.push(value)
        except IndexError:
            raise IndexError("Stack is empty")

    def nor(self, stack: Stack) -> None:
        """
        This method pops two values from the stack and pushes their NOR back to the stack
        :param stack: Stack object
        :return: None
        """
        try:
            value = not (stack.pop() or stack.pop())
            stack.push(value)
        except IndexError:
            raise IndexError("Stack is empty")
