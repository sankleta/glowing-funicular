class Solution:
    def peakIndexInMountainArray(self, arr):
        low = 0
        high = len(arr) - 1
        while low < high:
            middle = (high + low) // 2
            if arr[middle] < arr[middle + 1]:
                low = middle + 1
            else:
                high = middle
        return low


a = Solution()
print(a.peakIndexInMountainArray([3,4,5,1]))