class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        ind = arr.index(max(arr))
        count = 0
        flag = False

        if len(arr) >= 3:
            if ind == 0 or ind == len(arr)-1:
                return False
            else:
                for i in range(ind, 0, -1):
                    if arr[i] <= arr[i-1]:
                        return False
                    else:
                        flag = True
                if flag:
                    count +=1
                    flag=False

                for i in range(ind, len(arr)-1):
                    if arr[i] <= arr[i+1]:
                        return False
                    count += 1
                if count > 1:
                    return True

        else:
            return False
                    