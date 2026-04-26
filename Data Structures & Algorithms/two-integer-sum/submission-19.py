class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # get a hash which will have possible indicies
        # if first two are the pair that will be equal to target
        # otherwise find them one

        seen = {}

        for i in range(len(nums)):
            diff =  target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            seen[nums[i]] = i

