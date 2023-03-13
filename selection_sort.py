#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        return arr.index(min(arr))
            

    
    def selectionSort(self, arr,n):
        #code here
        for j in range(n):
            minn = self.select(arr[j:], j)
            minn+=j
            arr[j],arr[minn]=arr[minn],arr[j]
            # print(minn,arr)
