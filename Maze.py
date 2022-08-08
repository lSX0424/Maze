class Solution:
    def maze(self, maze: list[list[int]], start: list[int], destination: list[int]) -> bool:
        m, n, visit = len(maze), len(maze[0]), set()
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        stack = [start]
        while stack:
            curx, cury = stack.pop()
            if [curx, cury] == destination:
                    return True
            for dirx, diry in directions:
                tx, ty = curx, cury
                while 0 <= tx + dirx < m and 0 <= ty + diry < n and not maze[tx + dirx][ty + diry]:
                    tx, ty = tx + dirx, ty + diry
                if (tx, ty) not in visit:
                    visit.add((tx, ty))
                    stack.append((tx, ty))
        return False


solution=Solution()
#print(solution.maze([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],[0,4], [4,4]))

#print(solution.maze([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],[0,4],[3,2]))

print(solution.maze([[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]],[4,3], [0,1]))
