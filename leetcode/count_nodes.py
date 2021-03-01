import collections


class Solution:
    def count(self, depth):
        ans = 0
        for i in range(depth + 1):
            ans += 2 ** i
        return ans

    def countNodes(self, root):
        stack = collections.deque()
        stack.append((root, 0, 1))
        depth = 0
        while stack:
            dummy = stack.pop()
            depth = max(depth, dummy[1])
            if dummy[0].left is not None:
                stack.append((dummy[0].left, dummy[1] + 1, dummy[2] + 1))
                if dummy[0].right is not None:
                    stack.append((dummy[0].right, dummy[2] + 2))
                else:
                    return dummy[2] + 1
            else:
                if dummy[1] < depth:
                    return dummy[2]
        return self.count(depth)
