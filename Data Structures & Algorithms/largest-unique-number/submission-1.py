class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counts = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        unique_numbers = [num for num, count in counts.items() if count == 1]

        if not unique_numbers:
            return -1
        return max(unique_numbers)