class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        visited = set()
        cols = len(grid[0])
        rows = len(grid)
        # BFS Solution
        def bfs(r,c):
           queue = deque()
           queue.append((r,c))
           while queue:
            tr, tc = queue.popleft()
            if (0 <= tr < rows and 0 <= tc < cols) and (tr,tc) not in visited and grid[tr][tc]=="1":
                visited.add((tr,tc))
                queue.append((tr+1, tc))
                queue.append((tr, tc+1))
                queue.append((tr-1, tc))
                queue.append((tr, tc-1))
        islands=0
        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visited and grid[i][j]=="1":
                    islands+=1
                    bfs(i, j)
        return islands
