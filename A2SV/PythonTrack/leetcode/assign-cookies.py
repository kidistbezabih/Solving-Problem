class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count, j = 0, 0

        for i in range(len(g)):
            while j < len(s):
                if s[j] >= g[i]:
                    count += 1
                    j += 1
                    break
                else:
                    j+=1

        # print(g, s)
        # count, i, j= 0, 0, 0
        # while i < len(g):
        #     x = 0
        #     while j <len(s):
        #         if  s[j] >= g[i]:
        #             count += 1
        #             j+=1
        #             break
        #         else:
        #             return count
        #     i+=1
        return count