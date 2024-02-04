class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        while i < len(name) and j < len(typed):
            count1 = count2 = 0
            if name[i] != typed[j]:
                return False
            while i+1 < len(name) and name[i] == name[i+1]:
                count1 += 1
                i+=1
            count1 += 1
            i+=1

            while j+1 < len(typed) and typed[j] == typed[j+1]:
                count2 += 1
                j+=1
            count2 += 1
            j+=1

            if count2 < count1:
                return False
        
        if j < len(typed) or i < len(name):
            return False
        return True

        # i, j = 0, 0
        # while i < len(name) and j < len(typed):
        #     count1 = 1
        #     count2 = 1
        #     while i+1 < len(name) and name[i] == name[i+1]:
        #         count1 += 1
        #         i+=1

        #     while j+1 < len(typed) and typed[j] == typed[j+1]:
        #         count2 += 1
        #         j+=1

        #     if count2 < count1:
        #         return False
        #     i += 1
        #     j += 1
        # return True


        # while j < len(typed) and i < len(name):
        #     if typed[j] == name[i]:
        #         j+=1
        #         if i < len(name)-1 and name[i+1] == name[i] and j < len(typed) -1 and typed[j] == typed[j+1]:
        #             i+=1
        #     else:
        #         i+=1
        #         if name[i] != typed[j]:
        #             return False
        # return True