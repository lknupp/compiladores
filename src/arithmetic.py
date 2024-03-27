from .stack import Stack


class Arithmetic:
    """
    This class contains methods for arithmetic operations
    """

    def add(self, stack: Stack) -> None:
        """
        This method pops two values from the stack and pushes their sum back to the stack
        :param stack: Stack object
        :return: None
        """
        try:
            value = stack.pop() + stack.pop()
            stack.push(value)
        except IndexError:
            raise IndexError("Stack is empty")

    def subtract(self, stack: Stack):
        """
        This method pops two values from the stack and pushes their difference back to the stack
        :param stack: Stack object
        :return: None
        """
        try:
            value = stack.pop() - stack.pop()
            stack.push(value)
        except IndexError:
            raise IndexError("Stack is empty")

    def multiply(self, stack: Stack):
        """
        This method pops two values from the stack and pushes their product back to the stack
        :param stack: Stack object
        :return: None
        """
        try:
            value = stack.pop() * stack.pop()
            stack.push(value)
        except IndexError:
            raise IndexError("Stack is empty")

    def divide(self, stack: Stack):
        """
        This method pops two values from the stack and pushes their quotient back to the stack
        :param stack: Stack object
        :return: None
        """
        try:
            value = stack.pop() / stack.pop()
            stack.push(value)
        except IndexError:
            raise IndexError("Stack is empty")
        except ZeroDivisionError:
            raise ZeroDivisionError("Cannot divide by zero")

    def modulo(self, stack: Stack):
        """
        This method pops two values from the stack and pushes their modulo back to the stack
        :param stack: Stack object
        :return: None

        """
        try:
            value = stack.pop() % stack.pop()
            stack.push(value)
        except IndexError:
            raise IndexError("Stack is empty")
        except ZeroDivisionError:
            raise ZeroDivisionError("Cannot divide by zero")
