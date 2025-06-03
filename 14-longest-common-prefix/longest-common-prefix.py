class TrieNode:
    def __init__(self):
        self.children = defaultdict(int)
        self.isEnd = False
        self.linkCount = 0

    # def 

class Trie:
    def __init__(self):
        self.root  = TrieNode()

    def insert(self, word):
        curr = self.root

        for c in word:
            if c not in curr.children :
                curr.children[c] = TrieNode()
                curr.linkCount += 1

            curr = curr.children[c]
        curr.isEnd = True

    def search(self):
        curr = self.root

        ans = []

        while curr.linkCount == 1 and not curr.isEnd:
            prefix = list(curr.children.keys())[0]
            ans.append(prefix)
            curr = curr.children[prefix]
        return "".join(ans)


            

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        for word in strs:
            if not word:
                return ""
            trie.insert(word)
        
        return trie.search()