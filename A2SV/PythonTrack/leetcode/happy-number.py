class Solution:
    def isHappy(self, n: int) -> bool:
        st = set()
        while n != 1:
            if n in st:
                return False

            else:
                st.add(n)
                new_s = 0
                for i in str(n):
                    new_s += int(i) **2
                n = new_s
                
        return True

