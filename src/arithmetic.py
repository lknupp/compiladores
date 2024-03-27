from abc import ABC, abstractmethod
from .stack import Stack


class Arithmetic(ABC):
    """
    This class contains methods for arithmetic operations
    """
    @abstractmethod
    def add(stack: Stack) -> None:
        """
        This method pops two values from the stack and pushes their sum back to the stack
        :param stack: Stack object
        :return: None
        """
        try:
            result: int = stack.pop() + stack.pop()
            stack.push(result)
        except IndexError:
            raise IndexError("Stack is empty")

    @abstractmethod
    def subtract(stack: Stack):
        """
        This method pops two values from the stack and pushes their difference back to the stack
        :param stack: Stack object
        :return: None
        """
        try:
            result: int = stack.pop() - stack.pop()
            stack.push(result)
        except IndexError:
            raise IndexError("Stack is empty")

    @abstractmethod
    def multiply(stack: Stack):
        """
        This method pops two values from the stack and pushes their product back to the stack
        :param stack: Stack object
        :return: None
        """
        try:
            result: int = stack.pop() * stack.pop()
            stack.push(result)
        except IndexError:
            raise IndexError("Stack is empty")

    @abstractmethod
    def divide(stack: Stack):
        """
        This method pops two values from the stack and pushes their quotient back to the stack
        :param stack: Stack object
        :return: None
        """
        try:
            result: int = stack.pop() // stack.pop()
            stack.push(result)
        except IndexError:
            raise IndexError("Stack is empty")
        except ZeroDivisionError:
            raise ZeroDivisionError("Cannot divide by zero")

    @abstractmethod
    def modulo(stack: Stack):
        """
        This method pops two values from the stack and pushes their modulo back to the stack
        :param stack: Stack object
        :return: None

        """
        try:
            result: int = stack.pop() % stack.pop()
            stack.push(result)
        except IndexError:
            raise IndexError("Stack is empty")
        except ZeroDivisionError:
            raise ZeroDivisionError("Cannot divide by zero")
