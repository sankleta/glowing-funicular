class Solution:
    def findMissingRanges(self, nums, lower, upper):
        ans = []
        match = False
        starting_index = None
        if nums:
            for i in range(0, len(nums)):
                if lower == nums[i]:
                    match = True
                    starting_index = i
                    break
                elif lower < nums[i] <= upper:
                    match = True
                    starting_index = i
                    if nums[i] - lower == 1:
                        ans.append(str(lower))
                    else:
                        ans.append("{}->{}".format(lower, nums[i] - 1))
                    break

            if not match:
                if lower == upper:
                    return [str(lower)]
                return ["{}->{}".format(lower, upper)]
            else:
                for i in range(starting_index, len(nums)):
                    if i <= upper:
                        if i - 1 >= starting_index:
                            if nums[i] - nums[i - 1] == 2:
                                ans.append(str(nums[i] - 1))
                            elif nums[i] - nums[i - 1] > 2:
                                ans.append("{}->{}".format(nums[i - 1] + 1, nums[i] - 1))
                    else:
                        if i - 1 >= starting_index:
                            if upper - nums[i - 1] == 1:
                                ans.append(str(upper))
                            elif upper - nums[i - 1] > 1:
                                ans.append("{}->{}".format(nums[i - 1] + 1, upper))
                        break
                if upper - nums[-1] == 1:
                    ans.append(str(upper))
                elif upper - nums[-1] > 1:
                    ans.append("{}->{}".format(nums[-1] + 1, upper))
                return ans
        else:
            if lower == upper:
                return [str(lower)]
            return ["{}->{}".format(lower, upper)]


a = Solution()
print(a.findMissingRanges([-1], -9, -1))
