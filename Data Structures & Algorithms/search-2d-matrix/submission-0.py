class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m, n = len(matrix), len(matrix[0])
        
        left = 0
        right = (m * n) - 1

        while left <= right:
            mid = (right + left)//2 
            row = mid // n
            col = mid % n
            val = matrix[row][col]
            if target == val:
                return True
            elif target > val:
                left = mid + 1
            else:
                right = mid - 1

        return False