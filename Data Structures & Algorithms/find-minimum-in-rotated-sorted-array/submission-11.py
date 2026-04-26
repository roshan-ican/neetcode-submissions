class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        found = None
        small = 0
        if(len(nums) == 1 or len(nums) == 2):
            return min(nums)
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                found = i  # or nums[i] if you want the value
                print(found, "___x_")
                if low < found:
                    while (found <= high):
                        mid = (found + high) // 2
                        if mid > small:
                            small = mid
            else:
                return min(nums)
        return small
                