from pytest import mark, raises
from src.stack import Stack
from src.arithmetic import Arithmetic


@mark.arithmetic
@mark.add
class TestAddOperations:

    def test_when_the_stack_has_values_1_and_2_returns_3(self):
        first_value = 1
        second_value = 2
        total = first_value + second_value
        stack = Stack()
        stack.push(first_value)
        stack.push(second_value)

        Arithmetic.add(stack)

        assert stack.top() == total

    def test_when_the_stack_has_values_negative_2_and_negative_1_returns_negative_3(self):
        first_value = -2
        second_value = -1
        total = first_value + second_value
        stack = Stack()
        stack.push(first_value)
        stack.push(second_value)

        Arithmetic.add(stack)

        assert stack.top() == total

    def test_when_the_stack_is_empty_then_raises_index_error(self):
        stack = Stack()

        with raises(IndexError):
            Arithmetic.add(stack)

    def test_when_the_stack_has_only_one_value_then_raises_index_error(self):
        stack = Stack()
        stack.push(1)

        with raises(IndexError):
            Arithmetic.add(stack)


@mark.arithmetic
@mark.subtract
class TestSubtractOperations:

    def test_when_the_stack_has_values_2_and_1_returns_1(self):
        first_value = 2
        second_value = 1
        sub = first_value - second_value
        stack = Stack()
        stack.push(second_value)
        stack.push(first_value)

        Arithmetic.subtract(stack)

        assert stack.top() == sub

    def test_when_the_stack_has_values_1_and_2_returns_minus_1(self):
        first_value = 1
        second_value = 2
        sub = first_value - second_value
        stack = Stack()
        stack.push(second_value)
        stack.push(first_value)

        Arithmetic.subtract(stack)

        assert stack.top() == sub

    def test_when_the_stack_has_values_negative_1_and_1_returns_negative_2(self):
        first_value = -1
        second_value = 1
        sub = first_value - second_value
        stack = Stack()
        stack.push(second_value)
        stack.push(first_value)

        Arithmetic.subtract(stack)

        assert stack.top() == sub

    def test_when_the_stack_is_empty_then_raises_index_error(self):
        stack = Stack()

        with raises(IndexError):
            Arithmetic.subtract(stack)

    def test_when_the_stack_has_only_one_value_then_raises_index_error(self):
        stack = Stack()
        stack.push(1)

        with raises(IndexError):
            Arithmetic.subtract(stack)


@mark.arithmetic
@mark.multiply
class TestMultiplyOperations:
    def test_when_the_stack_has_values_2_and_3_returns_6(self):
        first_value = 2
        second_value = 3
        total = first_value * second_value
        stack = Stack()
        stack.push(second_value)
        stack.push(first_value)

        Arithmetic.multiply(stack)

        assert stack.top() == total

    def test_when_the_stack_has_values_negative_2_and_3_returns_negative_6(self):
        first_value = -2
        second_value = 3
        total = first_value * second_value
        stack = Stack()
        stack.push(second_value)
        stack.push(first_value)

        Arithmetic.multiply(stack)

        assert stack.top() == total

    def test_when_the_stack_has_values_negative_2_and_negative_3_returns_6(self):
        first_value = -2
        second_value = -3
        total = first_value * second_value
        stack = Stack()
        stack.push(second_value)
        stack.push(first_value)

        Arithmetic.multiply(stack)

        assert stack.top() == total

    def test_when_the_stack_is_empty_then_raises_index_error(self):
        stack = Stack()

        with raises(IndexError):
            Arithmetic.multiply(stack)

    def test_when_the_stack_has_only_one_value_then_raises_index_error(self):
        stack = Stack()
        stack.push(1)

        with raises(IndexError):
            Arithmetic.multiply(stack)

    def test_when_the_stack_has_values_0_and_3_returns_0(self):
        first_value = 0
        second_value = 3
        total = first_value * second_value
        stack = Stack()
        stack.push(second_value)
        stack.push(first_value)

        Arithmetic.multiply(stack)

        assert stack.top() == total


@mark.arithmetic
@mark.divide
class TestDivideOperations:
    def test_when_the_stack_has_values_6_and_3_returns_2(self):
        first_value = 6
        second_value = 3
        total = first_value // second_value
        stack = Stack()
        stack.push(second_value)
        stack.push(first_value)

        Arithmetic.divide(stack)

        assert stack.top() == total

    def test_when_the_stack_has_values_3_and_6_returns_0(self):
        first_value = 3
        second_value = 6
        total = first_value // second_value
        stack = Stack()
        stack.push(second_value)
        stack.push(first_value)

        Arithmetic.divide(stack)

        assert stack.top() == total

    def test_when_the_stack_has_values_negative_6_and_3_returns_negative_2(self):
        first_value = -6
        second_value = 3
        total = first_value // second_value
        stack = Stack()
        stack.push(second_value)
        stack.push(first_value)

        Arithmetic.divide(stack)

        assert stack.top() == total

    def test_when_the_stack_has_values_negative_3_and_6_returns_0(self):
        first_value = -3
        second_value = 6
        total = first_value // second_value
        stack = Stack()
        stack.push(second_value)
        stack.push(first_value)

        Arithmetic.divide(stack)

        assert stack.top() == total

    def test_when_the_stack_is_empty_then_raises_index_error(self):
        stack = Stack()

        with raises(IndexError):
            Arithmetic.divide(stack)

    def test_when_the_stack_has_only_one_value_then_raises_index_error(self):
        stack = Stack()
        stack.push(1)

        with raises(IndexError):
            Arithmetic.divide(stack)

    def test_when_the_stack_has_values_3_and_0_then_raises_zero_division_error(self):
        first_value = 3
        second_value = 0
        stack = Stack()
        stack.push(second_value)
        stack.push(first_value)

        with raises(ZeroDivisionError):
            Arithmetic.divide(stack)

    def test_when_the_stack_has_values_10_and_3_returns_3(self):
        first_value = 10
        second_value = 3
        total = first_value // second_value
        stack = Stack()
        stack.push(second_value)
        stack.push(first_value)

        Arithmetic.divide(stack)

        assert stack.top() == total


@mark.arithmetic
@mark.modulo
class TestModuloOperations:
    def test_when_the_stack_has_values_10_and_3_returns_1(self):
        first_value = 10
        second_value = 3
        total = first_value % second_value
        stack = Stack()
        stack.push(second_value)
        stack.push(first_value)

        Arithmetic.modulo(stack)

        assert stack.top() == total

    def test_when_the_stack_has_values_3_and_10_returns_3(self):
        first_value = 3
        second_value = 10
        total = first_value % second_value
        stack = Stack()
        stack.push(second_value)
        stack.push(first_value)

        Arithmetic.modulo(stack)

        assert stack.top() == total

    def test_when_the_stack_has_values_negative_10_and_3_returns_negative_1(self):
        first_value = -10
        second_value = 3
        total = first_value % second_value
        stack = Stack()
        stack.push(second_value)
        stack.push(first_value)

        Arithmetic.modulo(stack)

        assert stack.top() == total

    def test_when_the_stack_has_values_negative_3_and_10_returns_negative_3(self):
        first_value = -3
        second_value = 10
        total = first_value % second_value
        stack = Stack()
        stack.push(second_value)
        stack.push(first_value)

        Arithmetic.modulo(stack)

        assert stack.top() == total

    def test_when_the_stack_is_empty_then_raises_index_error(self):
        stack = Stack()

        with raises(IndexError):
            Arithmetic.modulo(stack)

    def test_when_the_stack_has_only_one_value_then_raises_index_error(self):
        stack = Stack()
        stack.push(1)

        with raises(IndexError):
            Arithmetic.modulo(stack)

    def test_when_the_stack_has_values_3_and_0_then_raises_zero_division_error(self):
        first_value = 3
        second_value = 0
        stack = Stack()
        stack.push(second_value)
        stack.push(first_value)

        with raises(ZeroDivisionError):
            Arithmetic.modulo(stack)

    def test_when_the_stack_has_values_0_and_3_returns_0(self):
        first_value = 0
        second_value = 3
        total = first_value % second_value
        stack = Stack()
        stack.push(second_value)
        stack.push(first_value)

        Arithmetic.modulo(stack)

        assert stack.top() == total
