from stack import Stack


def is_balanced(input_str):
    stack = Stack()
    for char in input_str:
        if char == '(':
            stack.push(char)
        elif char == ')':
            #if missing opening '('
            if stack.size() == 0:
                return False
            stack.pop()
    return stack.peek() is None