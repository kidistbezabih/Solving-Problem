class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        i = 0
        stack = []

        while i < len(s):
            if stack and s[i] == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
            i+=1
            print(i,stack)
        return len(stack)