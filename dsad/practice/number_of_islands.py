class Solution:
    
    def DFS(self, i, j):
        
        if i < 0 or j < 0 or i >= self.ROWS or j >= self.COLS or self.graph[i][j] == 0 or self.graph[i][j] == "0":
            return

        self.graph[i][j] = 0
        self.DFS(i - 1, j)
        self.DFS(i + 1, j)
        self.DFS(i, j - 1)
        self.DFS(i, j + 1)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        self.ROWS = len(grid)
        self.COLS = len(grid[0])
        self.graph = grid
        
        count = 0

        for i in range(self.ROWS):
            for j in range(self.COLS):
                # If a cell with value 1, then new island found
                if self.graph[i][j] == 1 or self.graph[i][j] == "1":
                    self.DFS(i, j)
                    count += 1
                    
        return count
        