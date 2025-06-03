class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if startGene == endGene:
            return 0
        wordSet = set(bank)
        steps = 0
        queue = deque([startGene])
        seen = set([startGene])

        while queue:
            for i in range(len(queue)):
                gene = queue.popleft()

                if gene == endGene:
                    return steps
                for j in range(8):
                    gns = set(['A', 'G', 'C', "T"])
                    gns.remove(gene[j])
                    for x in gns:
                        neighbor = gene[:j] + x+gene[j+1:]
                        if neighbor in wordSet and neighbor not in seen:
                            queue.append(neighbor)
                            seen.add(neighbor)
            steps += 1
        return -1