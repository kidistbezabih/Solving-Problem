class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        dct = {i:0 for i in range(1, n+1)}
        right, left = 0, 0
        logs = sorted(logs, key=lambda x:x[1])
        queries = sorted([(query, i) for i,query in enumerate(queries)])
        len_logs = len(logs)
        nullServers = n
        res = [0]*len(queries)

        for query, index in queries:
            while right < len_logs and logs[right][1] <= query:
                server = logs[right][0]
                if dct[server] == 0:
                    nullServers -= 1
                dct[server] += 1
                right += 1

            while left < len_logs and logs[left][1] < query-x:
                server = logs[left][0]
                dct[server] -= 1
                if dct[server] == 0:
                    nullServers += 1
                left += 1
            print(left, right)

            res[index] = nullServers
        return res            
            
