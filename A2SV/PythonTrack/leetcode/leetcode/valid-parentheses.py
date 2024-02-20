class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {'(': ')', '{': '}', '[': ']'}
        for i in s:
            if (i in d):
                stack.append(i)
            else:
                if (len(stack) > 0 and d[stack[-1]] == i):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
            