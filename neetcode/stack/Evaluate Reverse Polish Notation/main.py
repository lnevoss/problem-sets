class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0
        stack = []
        operands = ['+', '-', '*', '/']
        for token in tokens:
            if token.lstrip('-').isdigit():
                stack.append(int(token))
            elif token in operands:
                if len(stack) > 1:
                     b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(int(a / b))
                else:
                    return 0
        return stack[-1]