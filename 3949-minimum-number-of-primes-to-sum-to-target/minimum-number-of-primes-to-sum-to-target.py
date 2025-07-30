class Solution:
    def is_prime(self, num):
        if num < 2:
            return False

        for i in range(2, int(sqrt(num))+1):
            if num % i == 0:
                return False
        return True

    def mprimes(self, m):
        primes = []
        n = 0
        num = 2

        while n < m:
            if self.is_prime(num):
                primes.append(num)
                n += 1
            num += 1
        return primes
         
    def minNumberOfPrimes(self, n: int, m: int) -> int:
        m_primes = self.mprimes(m)
        dp = [float("inf")] * (n+1)
        dp[0] = 0


        for i in range(1, n+1):
            for prime in m_primes:
                if i - prime >= 0:
                    dp[i] = min(dp[i], dp[i-prime]+1)
        return dp[n] if dp[n] != float("inf") else -1
