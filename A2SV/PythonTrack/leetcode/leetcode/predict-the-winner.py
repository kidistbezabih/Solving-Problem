class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def winnerScore(nums, left, right):
            if left == right:
                return nums[left]

            return max((nums[left] - winnerScore(nums, left+1, right)), (nums[right] - winnerScore(nums, left, right-1)))
            
        return winnerScore(nums, 0, len(nums) - 1 ) >= 0
        
        