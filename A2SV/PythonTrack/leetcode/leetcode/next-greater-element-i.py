class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dictionary = {}
        stack = []
        ans = []

        for i in nums2:
            if not stack:
                stack.append(i)
            else:
                while stack and stack[-1] < i:
                    x =stack.pop()
                    dictionary[x] = i
                stack.append(i)

        for i in nums1:
            if i in dictionary:
                ans.append(dictionary[i])
            else:
                ans.append(-1)
        return ans