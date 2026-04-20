from typing import List


class Solution:
    def _dfs(self, isConnected, i, visited):
        for neighbor, connected in enumerate(isConnected[i]):
            if connected == 1 and neighbor not in visited:
                visited.add(neighbor)
                self._dfs(isConnected, neighbor, visited)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        count = 0

        for i in range(n):
            if i not in visited:
                count += 1
                visited.add(i)  # Mark the "start" of the province
                self._dfs(isConnected, i, visited)

        return count
