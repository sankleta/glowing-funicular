import collections


class Solution:
    def numIslands(self, grid):
        ans = 0
        rows = len(grid)
        columns = len(grid[0])
        stack = collections.deque()
        not_visited = set()
        for i in range(rows):
            for j in range(columns):
                not_visited.add((i, j))

        while not_visited:
            a = not_visited.pop()
            if grid[a[0]][a[1]] == '1':
                ans += 1
                stack.append(a)
                not_visited.add(a)
                while stack:
                    c = stack.pop()
                    if c in not_visited:
                        if grid[c[0]][c[1]] == '1':
                            if c[0] + 1 < rows:
                                stack.append((c[0] + 1, c[1]))
                            if c[0] - 1 >= 0:
                                stack.append((c[0] - 1, c[1]))
                            if c[1] + 1 < columns:
                                stack.append((c[0], c[1] + 1))
                            if c[1] - 1 >= 0:
                                stack.append((c[0], c[1] - 1))
                    not_visited.discard(c)
        return ans

a = Solution()
print(a.numIslands( [["1","1","0","0","0"], ["1","1","0","0","0"], ["0","0","1","0","0"], ["0","0","0","1","1"]]))