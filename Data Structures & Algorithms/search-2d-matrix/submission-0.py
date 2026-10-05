class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1

        while top <= bottom:
            mid = (top + bottom) // 2
            if matrix[mid][0] <= target <= matrix[mid][cols - 1]:
                left, right = 0, cols - 1

                while left <= right:
                    middle = (left + right) // 2
                    if matrix[mid][middle] == target:
                        return True
                    elif matrix[mid][middle] < target:
                        left = middle + 1
                    else:
                        right = middle - 1

                return False

            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                top = mid + 1

        return False


        
