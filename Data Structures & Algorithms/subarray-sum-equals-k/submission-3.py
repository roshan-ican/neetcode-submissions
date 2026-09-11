class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0:1}
        curr_sum = 0
        count = 0
        for i, n in enumerate(nums):
            curr_sum += n
            need = curr_sum - k
            if need in seen:
                count += seen[need]
            seen[curr_sum] = seen.get(curr_sum, 0) + 1
        return count
