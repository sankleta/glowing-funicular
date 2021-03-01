import collections


class Solution:
    def removeStones(self, stones):
        rows = collections.defaultdict(list)
        columns = collections.defaultdict(list)
        components = 0
        not_visited = set()
        for x, y in stones:
            rows[x].append((x, y))
            columns[y].append((x, y))
            not_visited.add((x, y))

        stack = collections.deque()
        while not_visited:
            stack.append(not_visited.pop())
            components += 1
            while stack:
                x, y = stack.pop()
                for a, b in rows[x]:
                    if (a, b) in not_visited:
                        stack.append((a, b))
                for a, b in columns[y]:
                    if (a, b) in not_visited:
                        stack.append((a, b))
                not_visited.discard((x, y))

        return len(stones) - components


c = Solution()
print(c.removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]]))
