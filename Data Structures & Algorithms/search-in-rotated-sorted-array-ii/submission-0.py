class Solution:
    def binary_search(self, arr, low, high, target):
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False



    def search(self, nums: List[int], target: int) -> bool:
        found = None # upper bound
        low = 0
        high = len(nums) - 1
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                found = i
                break
        if found is None:
            return self.binary_search(nums, low, high, target)
        elif target >= nums[0]:
            return self.binary_search(nums, 0, found, target)
        else:
            return self.binary_search(nums, found+ 1, high, target)


        