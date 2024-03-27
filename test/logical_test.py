from pytest import mark, raises
from src.stack import Stack
from src.logical import Logical


@mark.logical
@mark.and_
class TestAndOperations:

    def test_when_the_stack_has_values_10_and_1_returns_1(self):
        first_value = 10
        second_value = 1
        result = 1

        stack = Stack()
        stack.push(first_value)
        stack.push(second_value)

        Logical.and_(stack)
        print(stack.top())

        assert stack.top() == result

    def test_when_the_stack_has_values_99_and_0_returns_0(self):
        first_value = 99
        second_value = 0
        result = 0
        stack = Stack()
        stack.push(first_value)
        stack.push(second_value)

        Logical.and_(stack)

        assert stack.top() == result

    def test_when_the_stack_has_values_negative_12_and_negative_37_returns_1(self):
        first_value = -12
        second_value = -37
        result = 1
        stack = Stack()
        stack.push(first_value)
        stack.push(second_value)

        Logical.and_(stack)

        assert stack.top() == result

    def test_when_the_stack_is_empty_then_raises_index_error(self):
        stack = Stack()

        with raises(IndexError):
            Logical.and_(stack)

    def test_when_the_stack_has_only_one_value_then_raises_index_error(self):
        stack = Stack()
        stack.push(1)

        with raises(IndexError):
            Logical.and_(stack)

    def test_when_the_stack_has_two_values_and_logical_and_executed_stack_pointer_is_1(self):
        stack = Stack()
        for i in range(10):
            stack.push(i)

        Logical.and_(stack)

        assert stack.get_stack_pointer() == 9
