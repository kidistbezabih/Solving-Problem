class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        n = len(startTime)
        def sort_jobs():
            start_end_pair = sorted((startTime[i], endTime[i], profit[i]) for i in range(n))
            for i in range(n):
                startTime[i], endTime[i], profit[i] = start_end_pair[i]
        
        sort_jobs()

        @cache
        def dp(indx):
            if indx == n:
                return 0
            
            next_indx = bisect_left(startTime, endTime[indx])
            include = profit[indx] + dp(next_indx)
            exclude = dp(indx +1)
            return max(include, exclude)
        
        return dp(0)
        