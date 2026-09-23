class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        sublist = [n for s in matrix for n in s]
        
        left = 0
        right = len(sublist) - 1

        while left <= right:
            mid = (left + right) // 2
            if target == sublist[mid]:
                return True
            elif target > sublist[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return False
        