class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        res = 0

        while i < len(chars):
            group_length = 1

            while (i+group_length) < len(chars) and chars[i] == chars[i+group_length]:
                group_length += 1

            chars[res] = chars[i]
            res += 1
            if group_length > 1:
                index = list(str(group_length))
                chars[res:res + len(index)] = index
                res += len(index)
            i += group_length

        return res

                