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
            first_value = stack.pop()
            second_value = stack.pop()
            value = 1 if first_value or second_value else 0
            stack.push(int(value))
        except IndexError:
            raise IndexError("Stack is empty")

    @abstractmethod
    def not_(stack: Stack) -> None:
        """
        This method pops a value from the stack and if the value is non-zero, 
            pushes 0 onto the stack. Otherwise, pushes 1.
        :param stack: Stack object
        :return: None
        """
        try:
            value = 0 if stack.pop() else 1
            stack.push(value)
        except IndexError:
            raise IndexError("Stack is empty")

    @abstractmethod
    def xor(stack: Stack) -> None:
        """
        This method pops two values from the stack and pushes 1 if only one of the values is non-zero,
            otherwise pushes 0.
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
