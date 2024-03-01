class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }
        leng = len(digits)
        ans = []

        def magic(idx, path):
            if path and len(path) == leng:
                ans.append("".join(path[:]))
                return
            if idx >= leng:
                return
            for i in dic[int(digits[idx])]:
                path.append(i)
                magic(idx + 1, path)
                path.pop()

        magic(0, [])
        return ans
