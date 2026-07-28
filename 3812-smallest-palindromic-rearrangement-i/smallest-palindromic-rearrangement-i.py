class Solution:
    def smallestPalindrome(self, s: str) -> str:
        """
        
        count every character (n)
        sort based on the character (26)
        iterate over the dict and add half of every character to the list (n)
        is there is one odd character count put that the end and add the reverse (n)

        space = (26)
        """
        chrCount = Counter(s)

        chrCount = sorted(chrCount.items(), key=lambda x:x[0])
      
        left = [(items//2) * key for key, items in chrCount]
        partition = len(s)//2

        mid = "" if len(s) % 2 == 0 else s[partition]

        return "".join(left) + mid + "".join(left[::-1])
        

     
