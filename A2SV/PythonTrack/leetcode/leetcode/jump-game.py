class Solution:
    def canJump(self, nums: List[int]) -> bool:
        move=0
        nums[-1]  = float('inf')
        for i in range(len(nums)-1):
            move=max(move,nums[i])
            if move == 0:
                return False
            if move > 0:
                move -= 1
        return True