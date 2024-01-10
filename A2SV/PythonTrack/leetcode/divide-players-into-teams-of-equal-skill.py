class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        ln = len(skill)
        sm = skill[ln-1] + skill[0]
        product_sum = skill[ln-1] * skill[0]

        for i in range(1, ln//2):
            if sm != skill[i] + skill[ln-i-1]:
                return -1
            else:
                product_sum += skill[i] * skill[ln-i-1]
        return product_sum
            