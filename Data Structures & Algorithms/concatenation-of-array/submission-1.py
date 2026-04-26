class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        cp = nums[:]
        return nums + (cp)