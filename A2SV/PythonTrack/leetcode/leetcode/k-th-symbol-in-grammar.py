class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def kthGrammar(n, k):
            if n == 1:
                return 0
            
            mid = 2**(n-2)
            if k <= mid:
                return kthGrammar(n-1, k)
            else:
                return 1 - kthGrammar(n-1, k-mid)
        return kthGrammar(n, k) 
