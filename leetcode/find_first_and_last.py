class Solution:
    def binary_search(self, arr, target, is_left):
        low = 0
        high = len(arr)
        mid = 0
        while low < high:
            mid = (low + high) // 2
            if arr[mid] > target or (is_left and target == arr[mid]):
                high = mid
            else:
                low = mid + 1
        return low

    def searchRange(self, nums, target):
        left = self.binary_search(nums, target, True)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]

        return [left, self.binary_search(nums, target, False) - 1]


a = Solution()
print(a.searchRange([5, 7, 7, 8, 8, 10], 8))
