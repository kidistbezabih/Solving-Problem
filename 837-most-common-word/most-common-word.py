class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ans = ""
        max_count = 0
        count_word = defaultdict(int)
        banned = set(banned)
        buffer = []
        n = len(paragraph)

        for i, c in enumerate(paragraph):
            if c.isalnum():
                print(c)
                buffer.append(c.lower())
                if i != n-1:
                    continue
        
            if buffer:
                word = "".join(buffer)
                if word not in banned:
                    count_word[word] += 1
                    if max_count < count_word[word]:
                        ans = word
                        max_count = count_word[word]
            buffer = []
        return ans

