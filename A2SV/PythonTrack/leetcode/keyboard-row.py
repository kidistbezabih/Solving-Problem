class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        letter_lis = ["qwertyuiop", "asdfghjkl", "zxcvbnm" ]
        row_dictionary = dict()
        answer_list = []

        for i in range(3):
            for j in range(len(letter_lis[i])):
                row_dictionary[letter_lis[i][j]] = i

        for i in (words):
            flag = True
            row = row_dictionary[i[0].lower()]         
            for j in range(1, len(i)):
                if row_dictionary[i[j].lower()] != row:
                    flag = False
                    break
            if flag:
                answer_list.append(i)
                flag = True
        return answer_list            