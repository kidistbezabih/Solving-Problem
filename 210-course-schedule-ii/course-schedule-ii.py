class Solution:
    def topSort(self, node, graph, color, order):
        if color[node] == 1:
            return False
        if color[node] == 2:
            return True
        color[node] = 1
        for neig in graph[node]:
            if not self.topSort(neig, graph, color, order):
                return False
        color[node] = 2
        order.append(node)
        return True

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        color = [0 for _ in range(numCourses)]
        order = []

        for course, pre in prerequisites:
            graph[pre].append(course)

        for node in range(numCourses):
            if color[node] == 0:
                if not self.topSort(node, graph, color, order):
                    return []
        return order[::-1]