class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        lis = []
        lis2 = []
        for i in range(len(nums)):
            lis.append(-(nums[i]))

        for i in range(len(nums)):
            l = 0
            k = len(nums) - 1
            target = lis[i]
            while (l < k):
                if (i == k or i == l ):
                    if i == k:
                        k -= 1

                    else:
                        l += 1
                else:
                    if nums[l] + nums[k] < target:
                        l += 1
                    elif nums[l] + nums[k] > target:
                        k -= 1
                    else:
                        new_lis = (nums[l], nums[k], nums[i])
                        lis2.append(new_lis)
                        l+=1
                        k -= 1
   

        for i in range(len(lis2)):
            lis2[i] = sorted(lis2[i])
        lis2 = set(tuple(ls) for ls in lis2)
        return(list(i) for i in lis2)