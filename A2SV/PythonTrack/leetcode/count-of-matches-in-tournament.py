class Solution:
    def numberOfMatches(self, n: int) -> int:
        # def matchRound(teams):
        #     flag = False
        #     count = 0
        #     match = teams//2
        #     count += match
        #     while teams > 1:
        #         if match * 2 != teams:
        #             flag = True

        #         if flag == True and match % 2 == 1:
        #             teams = match + 1
        #             flag = False
        #         else:
        #             teams = match
        #         match = teams//2
        #         count += match
        #     return (count)
        # return (matchRound(n))

        tot = 0

        while n!= 1:
            if n%2:
                n = (n-1)//2
                tot += 1 + n
            else:
                n = n//2
                tot += n
        return tot