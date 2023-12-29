class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        my_destination_unit = abs(target[0]) + abs(target[1])
        for i in ghosts:
            if my_destination_unit >= abs(target[0] - i[0]) + abs(target[1] - i[1]):
                return False
        return True