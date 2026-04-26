class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen={}
        n = len(nums)
        for j in range(n):
            if nums[j] in seen and j - seen[nums[j]] <= k:
                return True
            seen[nums[j]] = j
        return False
      
        

        