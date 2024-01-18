class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        j = len(arr)-1
        ans = []

        while j != 0:
            if arr[j] > arr[0]:
                if j < len(arr)-1:
                    if arr[j] < arr[j+1]:
                        j-=1
                    else:
                        ## flip
                        arr[:j+1]=arr[:j+1][::-1]
                        ans.append(j+1)
                        j = len(arr)-1
                else:
                    j-=1
            else:
                ## flip
                arr[:j+1]=arr[:j+1][::-1]
                ans.append(j+1)
                j = len(arr)-1
        return ans