class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        diff = []
        for i in nums:
            diff.append(abs(i-nums[0]))
        tot = sum(diff)
        ans = [tot]
        n = len(diff)
        for i in range(1,n):
            ans.append(ans[-1] + (i) * abs(diff[i]-diff[i-1]) - (n-(i)) *abs(diff[i]-diff[i-1]))

        return ans