class Solution:
    def maxDistToClosest(self, seats):
        left = None
        ans = 0
        for right in range(len(seats)):
            if not seats[right]:
                if right != len(seats) - 1:
                    if left is None:
                        ans = max(ans, 1)
                        left = right
                    elif left == 0:
                        ans = max(ans, right - left + 1)
                else:
                    if left is not None:
                        ans = max(ans, right - left + 1)
                    else:
                        ans = max(ans, 1)
            else:
                if left is not None:
                    ans = max(ans, (right - left) // 2 + ((right - left) % 2 > 0))
                left = None
        return ans


c = Solution()
print(c.maxDistToClosest([0, 1, 0, 1, 0]))
