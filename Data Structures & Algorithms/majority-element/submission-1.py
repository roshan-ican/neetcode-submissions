class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        n = len(nums)
        more = n // 2
        mp = {}

        for n in nums:
            if n in mp:
                mp[n] += 1
            else:
                mp[n] = 1
            
            if mp[n] > more:
                return n
        