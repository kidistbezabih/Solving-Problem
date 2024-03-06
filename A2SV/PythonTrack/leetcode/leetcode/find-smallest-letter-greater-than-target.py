class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters)-1
        n = len(letters)
        if letters[right] <= target:
            return letters[0]

        while left <= right:
            mid = left + (right - left)//2
            if letters[mid] <= target:
                left = mid + 1
            elif letters[mid] > target:
                right =  mid - 1
        return letters[left]