class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        first_pointer, second_pointer = 0, 0
        n1 = len(word1)
        n2 = len(word2)
        string = ''

        while first_pointer < n1 and second_pointer < n2:
            if word1[first_pointer] > word2[second_pointer]:
                string += word1[first_pointer]
                first_pointer += 1

            elif word1[first_pointer] < word2[second_pointer]:
                string += word2[second_pointer]
                second_pointer += 1

            else:
                if word1[first_pointer+1:] > word2[second_pointer+1:]:
                    string += word1[first_pointer]
                    first_pointer += 1
                    
                else:
                    string += word2[second_pointer]
                    second_pointer+=1
        string += word1[first_pointer:]
        string += word2[second_pointer:]
        return string
