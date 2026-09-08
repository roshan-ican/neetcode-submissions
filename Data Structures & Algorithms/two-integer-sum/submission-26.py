class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, n in enumerate(nums):
            seen[n] = i

        for i in range(len(nums) - 1):
            if nums[i] + nums[i + 1] == target:
                return [i, i + 1]

            complacent = target - nums[i]
            if complacent in nums and seen[complacent] != i:
                return [i, seen[complacent]]



