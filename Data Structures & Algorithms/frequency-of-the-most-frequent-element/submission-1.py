class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # 124 5
        # 224 4
        # 324 3
        # 424 2
        # 434 1
        # 444 1
# K = 5
        # 1 4 8 13 - 5
        # 2 4 8 13 - 4
        # 3 4 8 13 - 3
        # 4 4 8 13 - 2
        nums.sort()
        res = 0
        total = 0
        l, r = 0, 0

        while r < len(nums):
            total += nums[r]

            while nums[r] * (r -l + 1) > total + k:
                total -= nums[l]
                l += 1
            res = max(res, r - l + 1)
            r+=1

        return res


