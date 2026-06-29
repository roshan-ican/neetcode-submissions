class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {0:1}
        total_valid_sums = 0
        current_sum = 0

        for i in range(len(nums)):
            current_sum += nums[i]
            if current_sum - k in prefix_sum:
                total_valid_sums += prefix_sum[current_sum - k]

            if current_sum in prefix_sum:
                prefix_sum[current_sum] += 1
            else:
                prefix_sum[current_sum] = 1
        return total_valid_sums

        