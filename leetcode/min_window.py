import collections


class Solution:
    def minWindow(self, s, t):
        left = 0
        right = 0
        ans = None
        t_count = collections.Counter(t)
        temp_count = collections.Counter()
        while left < len(s):
            if (t_count & temp_count) != t_count and right < len(s):
                temp_count[s[right]] += 1
                right += 1
            elif (t_count & temp_count) == t_count:
                if ans:
                    if len(ans) > right - left:
                        ans = s[left:right]
                else:
                    ans = s[left:right]
                temp_count[s[left]] -= 1
                left += 1
            else:
                break
        return ans


c = Solution()
print(c.minWindow("bbaac", "aba"))
