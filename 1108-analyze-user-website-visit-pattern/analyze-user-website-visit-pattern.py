class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        userPattern = defaultdict(list)
        pair = sorted([[timestamp[i], username[i], website[i]] for i in range(len(username))])

        for i in range(len(pair)):
            userPattern[pair[i][1]].append(pair[i][2])
        
        patterns = defaultdict(int)
        for username, web in userPattern.items():
            for i in set(combinations(web, 3)):
                patterns[i] += 1
            
        count, pat = 0, ()
        first_round = True

        for p, f in patterns.items():
            if first_round:
                first_round = False
                count, pat = f, p
            if count < f or (count == f and pat > p):
                pat = p
                count = f
        return pat

