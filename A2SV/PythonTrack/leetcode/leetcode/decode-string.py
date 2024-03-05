class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_string = ''
        current_num = 0

        for i in s:
            if i == '[':
                stack.append((current_string, current_num))
                current_string = ''
                current_num = 0
            elif i.isdigit():
                current_num = current_num * 10 + int(i)
            elif i == ']':
                prev_string, number = stack.pop()
                current_string = prev_string + current_string * number
            else:
                current_string += i
        return current_string  