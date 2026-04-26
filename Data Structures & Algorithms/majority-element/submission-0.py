class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # hash map and count the max of nums

        counter = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        most = max(counter, key = counter.get)
        return most
            
            