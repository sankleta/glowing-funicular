class Solution:

    def searchMatrix(self, matrix, target):
        if not matrix:
            return False

        def search(top, left, bottom, right):
            if top > bottom or right < left:
                return False
            elif target < matrix[top][left] or target > matrix[bottom][right]:
                return False

            mid = left + (right - left) // 2

            row = top
            while row <= bottom and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1

            return search(row, left, bottom, mid - 1) or search(top, mid + 1, row - 1, right)

        return search(0, 0, len(matrix) - 1, len(matrix[0]) - 1)


a = Solution()
print(a.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],21))