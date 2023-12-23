class Solution:
    def interpret(self, command: str) -> str:
        s = ''
        stack = []
        for i in command:
            if i == "G":
               s += i
            else:
                if stack == []:
                    stack.append(i)
                else:
                    if i == ")":
                        if stack[-1] == "(":
                            stack.pop()
                            s+="o"
                        else:
                            s+=''.join(stack[-2:])
                            for i in range(3):
                                stack.pop()
                    else:
                        stack.append(i)
        return s



       
       
       
       
        # stack = []
        # string = ""
        # for i in range(len(command)):
        #     # if stack == []:
        #     #     stack.append(command[i])
        #     # else:
        #         if command[i] == "(":
        #             stack.append(command[i])
        #         else:
        #             if command[i] == ")":
        #                 if stack[-1] == "(":
        #                     stack.pop()
        #                     string + "o"
        #                 else:
        #                     string = ''.join(stack[len(stack)-1: len(stack)-2])
        #                     stack.pop()
        #                     stack.pop()
        #                     stack.pop()
        # return(string)
