class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        lens = len(s)
        for i in range(lens):
            if(s[i] == '(' or s[i] == '{' or s[i] == '['):
                stack.append(s[i])
            elif (s[i] == ')' or s[i] == '}' or s[i] == ']'):
                stack.append(s[i])
                lenStack = len(stack)
                if (s[i] == ')' and stack[lenStack-2] == '('):
                    stack.pop()
                    stack.pop()
                if (s[i] == '}' and stack[lenStack-2] == '{'):
                    stack.pop()
                    stack.pop()
                if (s[i] == ']' and stack[lenStack-2] == '['):
                    stack.pop()
                    stack.pop()
        return len(stack) == 0
