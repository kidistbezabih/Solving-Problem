class Solution:
    def sortSentence(self, s: str) -> str:
        lis = s.split(' ')
        my_dict = {lis[i][-1]:lis[i][:-1] for i in range(len(lis))}
        keys = my_dict.keys()
        sorted_keys = sorted(keys)
        sorted_dict = {}
        for key in sorted_keys:
            sorted_dict[key] = my_dict[key]
        val = ' '.join(sorted_dict.values())
        return val