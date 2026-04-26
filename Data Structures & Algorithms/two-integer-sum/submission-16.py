class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for i, num in enumerate(nums):
            m = target - num
            if m in numMap:
                return [numMap[m], i]
            numMap[num] = i
        return []