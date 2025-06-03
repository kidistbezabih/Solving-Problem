class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start, end = [], []
        n = len(intervals)
        res = 0

        for i in range(len(intervals)):
            s, e = intervals[i]
            start.append((s, i))
            end.append((e, i))

        start.sort()
        end.sort()

        p1, p2 = 0, 0
        meetings = set()

        while p1 < n and p2 < n:
            if start[p1][0] < end[p2][0]:
                meetings.add(start[p1][1])
                p1 += 1
            elif start[p1][0] > end[p2][0]:
                meetings.remove(end[p2][1])
                p2 += 1
            else:
                meetings.add(start[p1][1])
                meetings.remove(end[p2][1])
                p1 += 1
                p2 += 1
            res = max(res, len(meetings))
        return res
