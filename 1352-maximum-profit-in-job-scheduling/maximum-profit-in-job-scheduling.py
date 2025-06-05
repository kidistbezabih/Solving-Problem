class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        n = len(startTime)
        def sort_jobs():
            start_end_pair = sorted((startTime[i], endTime[i], profit[i]) for i in range(n))
            for i in range(n):
                startTime[i], endTime[i], profit[i] = start_end_pair[i]
        
        sort_jobs()

        hash_map = defaultdict(int)
        curr_max = 0
        for i in range(n - 1, -1, -1):
            next_indx = bisect_left(startTime, endTime[i])
            include = profit[i] + hash_map[next_indx]
            curr_max = max(include, curr_max)
            hash_map[i] = curr_max
        
        return curr_max

        @cache
        def dp(indx):
            if indx == n:
                return 0
            
            next_indx = bisect_left(startTime, endTime[indx])
            include = profit[indx] + dp(next_indx)
            exclude = dp(indx + 1)
            return max(include, exclude)
        
        return dp(0)
        