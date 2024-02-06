# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
        # if t == "":
        #     return ""
        # countT, window = Counter(t), {}
        

        # have, need = 0, len(countT)
        # res, resLen = [-1, -1], float('inf')
        # for r in range(len(s)):
        #     c = s[r]
        #     window[c] = 1 + window.get(c, 0)

        #     if c in countT and window[c] == countT[c]:
        #         have += 1
        #     l=0
            
        #     while need == have:
        #         if r - l + 1 < resLen:
        #             res = [l,r]
        #             resLen = (r-l+1)
        #         window[s[l]] -= 1
        #         if s[l] in countT and window[s[l]] < countT[s[l]]:
        #             have -= 1
        #         l+=1
        #     l, r = res
        #     print(l, r)
        #     return s[l:r+1] if resLen != float('inf') else  ""




        # d1 = Counter(t)
        # d2 = defaultdict(int)
        # i , j = 0, 0
        # res = float('inf')
        # string = ''
        
        # while j  < len(s):
        #     d2[s[j]] += 1
        #     c = 0
        #     for k in d1:
        #         if k in d2 and d2[k] >= d1[k]:
        #             c+=1

        #     if c == len(t):
        #         d2[s[i]] -= 1
        #         if d2[s[i]] == 0:
        #             d2.pop(s[i])

        #         res = min(res, j-i+1)
        #         if res == j-i+1:
        #             string = s[i:j+1]
        #         i+=1
                
        #     else:
        #         j+=1
        #     print(string, i, j)
        # return res

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        map = [0] * 128
        count = len(t)
        start = 0
        end = 0
        min_len = float('inf')
        start_index = 0
        # UPVOTE !
        for char in t:
            map[ord(char)] += 1

        while end < len(s):
            if map[ord(s[end])] > 0:
                count -= 1
            map[ord(s[end])] -= 1
            end += 1

            while count == 0:
                if end - start < min_len:
                    start_index = start
                    min_len = end - start

                if map[ord(s[start])] == 0:
                    count += 1
                map[ord(s[start])] += 1
                start += 1

        return "" if min_len == float('inf') else s[start_index:start_index + min_len]