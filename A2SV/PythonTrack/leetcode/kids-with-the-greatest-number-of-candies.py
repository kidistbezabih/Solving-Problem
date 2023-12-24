class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        lis = []
        for i in candies:
            if i+extraCandies >= max_candies:
                lis.append(True)
            else:
                lis.append(False)
        return lis