import itertools

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        sub_matrix = [n for s in matrix for n in s]

        left = 0
        right = len(sub_matrix) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == sub_matrix[mid]:
                return True
            elif target > sub_matrix[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return False
