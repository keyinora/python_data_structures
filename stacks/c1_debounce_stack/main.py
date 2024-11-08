from stack import Stack


class DebounceStack(Stack):
    def push(self, action):
        if self.peek() == action:
            return
        super().push(action)