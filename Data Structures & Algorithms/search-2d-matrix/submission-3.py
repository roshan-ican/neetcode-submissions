import itertools
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat = list(itertools.chain.from_iterable(matrix))
    
        low = 0
        high = len(flat) - 1
        while low <= high:
            mid = (low + high) // 2
            if target == flat[mid]:
                return True
            elif target <= flat[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return False