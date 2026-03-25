class Solution:
    def _dfs(self, grid, r, c):
        # 1. BASE CASES: Stop if we are out of bounds or hit water
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == "0":
            return

        # 2. MARK AS VISITED: "Sink" the land by turning it to water
        grid[r][c] = "0"

        # 3. EXPLORE: Call DFS on all 4 neighbors
        self._dfs(grid, r + 1, c) # Down
        self._dfs(grid, r - 1, c) # Up
        self._dfs(grid, r, c + 1) # Right
        self._dfs(grid, r, c - 1) # Left

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    count+=1
                    self._dfs(grid, r, c)
            
        return count