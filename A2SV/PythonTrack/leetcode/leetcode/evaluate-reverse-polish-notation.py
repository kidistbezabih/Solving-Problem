class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == '+' or i == '-' or i == '*' or i == '/':
                b = stack.pop()
                a = stack.pop()
                op = i
                exp = str(a)+op+str(b)
                res = int(eval(exp))
                stack.append(res)

            else:
                stack.append(i) 
        return int(stack[-1])