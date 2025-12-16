class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []

        for x in nums:
            cur = x
            # Try to merge with previous elements while gcd > 1
            while stack:
                g = gcd(stack[-1], cur)
                if g == 1:
                    break
                # Replace the two numbers with their LCM
                # LCM(a, b) = a // gcd(a, b) * b
                cur = stack[-1] // g * cur
                stack.pop()
            stack.append(cur)

        return stack
        