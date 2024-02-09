class NumArray:

    def __init__(self, nums: List[int]):
        self.queue = nums
        for i in range(1, len(nums)):
            self.queue[i] =self.queue[i] + self.queue[i-1] 

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.queue[right]
        return self.queue[right] - self.queue[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)