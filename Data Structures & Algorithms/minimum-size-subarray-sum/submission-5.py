class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0

        length = float('inf')
        l = 0
        r = 0
        count_sum=0
        while r < len(nums):
            count_sum+=nums[r]
            r+=1
            while count_sum >= target:
                length = min(length, r - l)
                count_sum-=nums[l]
                l+=1

        return length


# target=7
# nums=[,1,2,4,3]
#             r