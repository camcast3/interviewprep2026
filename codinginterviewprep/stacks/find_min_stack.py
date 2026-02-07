class Stack:
    def __init__(self):
        self.public_stack = []
        self.min_stack = []

    def pop(self):
        if len(self.public_stack) == 0:
            return -1

        popped_value = self.public_stack.pop()
        if self.min_stack[-1] == popped_value:
            self.min_stack.pop()

        return popped_value

    def push(self, value):
        if not self.min_stack or self.min_stack[-1] >= value:
            self.min_stack.append(value)

        self.public_stack.append(value)

    def min(self):
        if len(self.min_stack) == 0:
            return -1

        return self.min_stack[-1]


stack_1 = Stack()

stack_1.push(3)
stack_1.push(2)
stack_1.push(1)

print(f"What is the min in stack_1: {stack_1.min()}")

print(f"What value was just poped from stack_1: {stack_1.pop()}")

print(f"What is the min in stack_1 after one pop: {stack_1.min()}")

stack_2 = Stack()

print(f"What is the min in stack_2: {stack_2.min()}")

print(f"What value was just poped from stack_2: {stack_2.pop()}")

print(f"What is the min in stack_2 after one pop: {stack_2.min()}")

stack_3 = Stack()
stack_3.push(40)
stack_3.push(30)

print(f"What is the min in stack_2: {stack_3.min()}")

print(f"What value was just poped from stack_2: {stack_3.pop()}")

print(f"What is the min in stack_2 after one pop: {stack_3.min()}")
