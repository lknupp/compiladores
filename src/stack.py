

class Stack:
    def __init__(self) -> None:
        self.stack = list()
        self.program_counter = 0
        self.frame_base_register = 0

    def push(self, value: int) -> None:
        self.stack.append(value)

    def pop(self) -> int:
        return self.stack.pop()

    def get_stack_pointer(self) -> int:
        return len(self.stack)
