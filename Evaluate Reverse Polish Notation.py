class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        exp = ''
        stack = []
        result = 0
        operator = '+-/*'
        toklens = len(tokens)
        for i in range(toklens):
            if (tokens[i] not in operator):
                stack.append(tokens[i])
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if tokens[i] == '+':
                    stack.append(a+b)
                if tokens[i] == '-':
                    stack.append(a-b)
                if tokens[i] == '*':
                    stack.append(a*b)
                if tokens[i] == '/':
                    stack.append(int(a/b))
        return int(stack.pop())
