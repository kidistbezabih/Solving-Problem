class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        for count, char in [(-a, 'a'),(-b, 'b'),(-c, 'c')]:
            if count:
                heappush(heap, (count, char))

        ans = []
        while heap:
            count1, char1 = heappop(heap)
            if len(ans) > 1 and ans[-1] == ans[-2] == char1:
                if not heap:
                    break
                count2, char2 = heappop(heap)
                ans.append(char2)
                count2 += 1
                if count2:
                    heappush(heap, (count2, char2))
            else:
                ans.append(char1)
                count1 += 1
            if count1:
                heappush(heap, (count1, char1))            
        return "".join(ans)

