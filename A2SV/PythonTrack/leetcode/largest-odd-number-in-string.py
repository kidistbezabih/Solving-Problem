class Solution:
    def largestOddNumber(self, num: str) -> str:
      ln = len(num)-1
      while ln >= 0:
        if int(num[ln]) % 2 == 1:
          return num[:ln+1]
        else:
          ln -=1
      return ''
