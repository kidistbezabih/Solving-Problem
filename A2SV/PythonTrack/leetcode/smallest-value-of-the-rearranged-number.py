class Solution:
    def smallestNumber(self, num: int) -> int:
        s = str(num)
        positive = True

        if num >= 0:
            s = sorted(s)
        else:
            s = sorted(s[1:])[::-1]
            positive= False

        if s[0] == '0':
            for i in range(len(s)):
                if s[i] != '0':
                    print(i, 'fkjd')
                    s[0], s[i] = s[i], s[0]
                    break
        if positive:
            return int(''.join(s))
        return int('-'+''.join(s))
        