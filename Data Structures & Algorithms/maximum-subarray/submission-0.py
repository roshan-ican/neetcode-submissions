class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float('-inf')
        n = len(nums)
        for i in range(n):
            for j in range(i,n):
                cur_sum = 0
                for k in range(i, j + 1):
                    cur_sum += nums[k]
                maxi = max(maxi, cur_sum)
        return maxi