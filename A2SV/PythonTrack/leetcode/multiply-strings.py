import decimal
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def intOf(ch):
            return ord(ch) - 48
        def charOf(x):
            return chr(x + 48)
            
        if num1 == '0' or num2 == '0':
            return '0'
        else:
            m = len(num2)
            n = len(num1)
            answer = [0] * (m+n)
            for i in range(m-1, -1, -1):
                carry = 0
                ind = 0
                result = [0] * (m+n)
                for j in range(n - 1, -1, -1):
                    ind = i+j+1 
                    product = intOf(num1[j]) * intOf(num2[i])
                    result[ind] = carry + product%10
                    carry = product // 10
                if carry >= 1:
                    result[ind-1] += carry
        
                carry = 0
                for j in range(len(answer)-1, -1, -1):
                    s = carry + answer[j] + result[j]
                    answer[j] = s%10
                    carry = s//10
                    if carry > 1:
                        x = j

                if carry >= 1:
                    answer[x] += carry  
                string = ''
                for j in range(len(answer)):
                    string += charOf(answer[j])
                x = 0
                for j in string:
                    if j == '0':
                        x += 1
                    else: break

            return string[x:]
                