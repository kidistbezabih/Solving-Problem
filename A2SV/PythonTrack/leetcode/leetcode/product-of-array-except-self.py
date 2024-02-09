class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        prefixProduct = []
        sufixProduct = []
        lis = []
        for i in nums:
            product *= i 
            prefixProduct.append(product)
        print(prefixProduct)
        product = 1

        for i in range(len(nums) - 1, -1, -1):
            product *= nums[i] 
            sufixProduct.append(product)
        sufixProduct = (sufixProduct[::-1])
        print(sufixProduct)
        lis.append(sufixProduct[1])
        
        for i in range(1, len(nums)-1):
            lis.append(sufixProduct[i + 1] * prefixProduct[i - 1])
        lis.append(prefixProduct[len(prefixProduct) - 2])
        return(lis)