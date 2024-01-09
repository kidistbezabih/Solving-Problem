class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        lis = [str(i) for i in nums]
        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1

        lis = sorted(lis, key = cmp_to_key(compare))
        return str(int(''.join(lis)))