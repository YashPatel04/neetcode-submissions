class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minheap = [(grid[0][0],0,0)]
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        time = 0
        prev = 0
        while minheap:
            d, tr, tc = heapq.heappop(minheap)
            if(tr, tc)==(ROWS-1, COLS-1): return max(time, d)
            if (tr, tc) in visited:
                continue
            time=d
            visited.add((tr,tc))
            # up, down, left, right
            up = (tr-1,tc) if tr!=0 else None
            down = (tr+1,tc) if tr!=ROWS-1 else None
            left = (tr,tc-1) if tc!=0 else None
            right = (tr,tc+1) if tc!=COLS-1 else None
            if up:
                heapq.heappush(minheap,(max(grid[up[0]][up[1]], d), up[0], up[1]))
            if down:
                heapq.heappush(minheap,(max(grid[down[0]][down[1]], d), down[0], down[1]))
            if left:
                heapq.heappush(minheap,(max(grid[left[0]][left[1]], d), left[0], left[1]))
            if right:
                heapq.heappush(minheap,(max(grid[right[0]][right[1]], d), right[0], right[1]))
        return time