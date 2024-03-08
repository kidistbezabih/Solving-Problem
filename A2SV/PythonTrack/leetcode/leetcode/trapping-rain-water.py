class Solution:
    def trap(self, nums: List[int]) -> int:
        stack =[]
        vol = 0
        _sum = 0

        for i in range(len(nums)):
            if not stack:
                stack.append((nums[i], i))
            else:
                if stack[-1][0] > nums[i]:
                    stack.append((nums[i], i))
                else:
                    while len(stack) > 1 and nums[i] > stack[-1][0]:
                        _sum +=stack.pop()[0]
                    if len(stack) == 1 and stack[0][0] < nums[i]:
                        vol += ((i-stack[0][1]-1) * stack[0][0]) - _sum
                        _sum = 0
                        stack.pop()
                    stack.append((nums[i], i))
                    
        for i in range(1 , len(stack)):
            vol += (stack[i][1] - stack[i-1][1] -1) * min(stack[i][0], stack[i-1][0])
        vol -= _sum
        
        return vol