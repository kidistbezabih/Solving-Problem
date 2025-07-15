class Solution:
    def generate_primes(self, m):
        primes = []
        i = 2
        while len(primes) < m:
            if self.is_prime(i):
                primes.append(i)
            i+=1
        return primes

    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(sqrt(num))+1):
            if  num % i == 0:
                return False
        return True

    def minNumberOfPrimes(self, n: int, m: int) -> int:
        mprimes = self.generate_primes(m)
        dp = [float('inf')]*(n+1)
        dp[0] = 0

        for prime in mprimes:
            for i in range(prime, n+1):
                dp[i] = min(dp[i], dp[i-prime] + 1)

        return dp[n] if dp[n] != math.inf else -1

