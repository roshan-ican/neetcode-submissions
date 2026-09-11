class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #     map = {}
        #     for i in range(len(nums) - 1):
        #         s = nums[i] + nums[i + 1]
        #         if s == target:
        #             return [i, i + 1]

        #         complacent = target - nums[i]
        #         if complacent in map:
        #             return [map[complacent], i]
        #         map[nums[i]] = i
        #         class Solution:
        # def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            complacent = target - nums[i]
            if complacent in map:
                return [map[complacent], i]
            map[nums[i]] = i
        return []