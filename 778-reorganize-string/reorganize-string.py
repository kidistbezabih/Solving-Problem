class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        char_count = Counter(s)
        max_count, letter = 0, ''

        for char, count in char_count.items():
            if count > max_count:
                max_count = count
                letter = char
        if max_count > (n+1) // 2:
            return ""
        
        index = 0
        ans = [''] * n
        while char_count[letter] != 0:
            ans[index] = letter
            index += 2
            char_count[letter] -= 1

        for char, count in char_count.items():
            while count >  0:
                if index > n-1:
                    index = 1
                ans[index] = char
                index += 2
                count -= 1
        return ''.join(ans)