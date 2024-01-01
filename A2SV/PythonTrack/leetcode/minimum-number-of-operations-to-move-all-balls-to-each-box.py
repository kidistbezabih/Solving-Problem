class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        lis = []
        for i in range(len(boxes)):
            tot_path = 0
            for j in range(len(boxes)):
                if boxes[j] == '1':
                    tot_path += abs(j-i)
            lis.append(tot_path)
        return lis 