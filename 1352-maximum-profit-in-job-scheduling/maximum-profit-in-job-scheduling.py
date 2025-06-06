class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)

        job_schedule = sorted([(startTime[i], endTime[i], profit[i]) for i in range(n)])
        startTime = [i[0] for i in job_schedule ]
        memo = {}

        def dp(i):
            if i in memo:
                return memo[i]
            if i == n:return 0
            l,r = i+1, n-1
            next_index = bisect_left(startTime, job_schedule[i][1])

            memo[i] =  max( job_schedule[i][2]+ dp(next_index), dp(i+1))
            return memo[i]
        return dp(0)