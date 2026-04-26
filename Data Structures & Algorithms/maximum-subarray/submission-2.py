class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float('-inf')
        n = len(nums)
        for i in range(n):
            cur_sum = 0
            for j in range(i,n):
                cur_sum += nums[j]
                maxi = max(maxi, cur_sum)
        return maxi