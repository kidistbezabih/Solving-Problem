class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        dct = Counter(arr)
        x = max(dct.values())
        for key, value in dct.items():
            if value == x:
                return key