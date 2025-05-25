class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for i in range(numCourses)]
        order = []
        indegree = [0] * numCourses
        queue = deque()

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            pre = queue.popleft()
            order.append(pre)
            for course in graph[pre]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)
        return order if len(order) == numCourses else []
            