class Solution:
    def balancedString(self, s: str) -> int:
        counter = Counter(s)
        k = len(s)//4
        req_counter = defaultdict(int)
        
        for i in counter:
            if counter[i] - k > 0:
                req_counter[i] += (counter[i] - k)
        
        if len(req_counter) == 0:
            return 0
        i = 0
        res = len(s)
        for j in range(len(s)):
            if s[j] in req_counter:
                req_counter[s[j]] -= 1
            
            while max(req_counter.values()) <= 0:
                res = min(res, j-i+1)
                if s[i] in req_counter:
                    req_counter[s[i]] += 1
                i += 1
        return res