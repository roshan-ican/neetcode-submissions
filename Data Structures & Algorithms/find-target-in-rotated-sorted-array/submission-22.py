class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid

            if nums[lo] <= nums[mid]:            # left side is sorted
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1                  # target is in left side
                else:
                    lo = mid + 1
            else:                                 # right side is sorted
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1                  # target is in right side
                else:
                    hi = mid - 1
        return -1