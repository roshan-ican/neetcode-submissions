class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            if val == nums[i]:
                nums[i] = '_'
        count = [num for num in nums if num != '_']
        nums[:len(count)] = count
        return len(count)
