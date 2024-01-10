class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse = True)
        processorTime.sort()
        ln  = len(tasks)
        mx = 0

        for i in range(ln):
            mx = max(mx, tasks[i] + (processorTime[i//4]))
        return mx