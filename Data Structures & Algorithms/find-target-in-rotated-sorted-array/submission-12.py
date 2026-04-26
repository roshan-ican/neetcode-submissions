class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        
        # Find pivot where rotation happens
        found = -1
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                found = i
                break
        
        def binary_search(low, high):
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    return mid
                elif target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            return -1
        
        if found == -1:
            # Array not rotated, search entire array
            return binary_search(low, high)
        
        # If target in left sorted portion
        if nums[0] <= target <= nums[found]:
            return binary_search(0, found)
        else:
            # Target in right sorted portion
            return binary_search(found + 1, len(nums) - 1)
