class Solution:
    def simplifyPath(self, path: str) -> str:
        directory_list = path.split('/')
        stack = []

        for i in directory_list:
            if i == '..':
                if stack:
                    stack.pop()
            elif i == '' or i == '.':
                continue
            else:
                stack.append(i)
        return '/'+'/'.join(stack)