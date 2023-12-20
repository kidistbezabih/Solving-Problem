class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool0
        """
        reverse = 0
        n = x
        if (x < 0):
            x *= -1
        while x > 0:
            reminder =  x % 10
            reverse = reverse * 10 + reminder
            x = x / 10
        if (n < 0):
            result = str(reverse) + '-'
            reverse = result
            
        if reverse == n:
            return True
        else:
            return False