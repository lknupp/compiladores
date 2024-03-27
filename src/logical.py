from .stack import Stack
from abc import ABC, abstractmethod


class Logical(ABC):
    """
    This class contains methods for logical operations
    """
    @abstractmethod
    def and_(stack: Stack) -> None:
        """
        This method pops two values from the stack and pushes their logical AND back to the stack
        :param stack: Stack object
        :return: None
        """
        try:
            value = 1 if stack.pop() and stack.pop() else 0
            stack.push(int(value))
        except IndexError:
            raise IndexError("Stack is empty")

    @abstractmethod
    def or_(stack: Stack) -> None:
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

    @abstractmethod
    def not_(stack: Stack) -> None:
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

    @abstractmethod
    def xor(stack: Stack) -> None:
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

    @abstractmethod
    def nand(stack: Stack) -> None:
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

    @abstractmethod
    def nor(stack: Stack) -> None:
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
