class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        word = []
        wordList = defaultdict(int)
        banned = set(banned)
        mx_freq = 0
        ans = ""

        for i, char in enumerate(paragraph):
            if char.isalpha():
                word.append(char.lower())
            if char == " " or  i == len(paragraph)-1 or char == ',':
                w = ''.join(word)
                if w and w not in banned:
                    wordList[w] += 1
                    if wordList[w] > mx_freq:
                        mx_freq = wordList[w]
                        ans = w
                word = []

        return ans
            
