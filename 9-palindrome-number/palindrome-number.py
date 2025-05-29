class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        inverted = 0
        original = x
        while x:
            inverted = inverted * 10 + x%10
            x//=10

        return original == inverted