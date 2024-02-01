class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o' , 'u'}
        vowel_count = 0
        for i in range(k):
            if s[i] in vowels:
                vowel_count += 1
        res = vowel_count

        i, j = 0, k
        while j < len(s):
            if s[i] in vowels:
                vowel_count -= 1
            if s[j] in vowels:
                vowel_count += 1
            res= max(res,vowel_count)
            i += 1
            j += 1
        return res

