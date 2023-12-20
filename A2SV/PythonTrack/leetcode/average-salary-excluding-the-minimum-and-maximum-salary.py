class Solution:
    def average(self, salary: List[int]) -> float:
        min_salary = min(salary)
        max_salary = max(salary)
        ln = len(salary)
        total = 0
        for i in salary:
            if i != min_salary and i != max_salary:
                total += i
        return total / (ln-2)
