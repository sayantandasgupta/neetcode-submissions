class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1
        row = -1

        while top <= bottom:
            row = (top + bottom) // 2

            if matrix[row][0] <= target <= matrix[row][cols - 1]:
                break
            elif matrix[row][0] > target:
                bottom = row - 1
            else:
                top = row + 1

        if not top <= bottom:
            return False

        left, right = 0, cols - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


        
