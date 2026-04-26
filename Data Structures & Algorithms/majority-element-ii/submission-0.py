class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        n = len(nums)
        k = n // 3
        print(k)
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        print(freq)
        res = []
        for key,val in freq.items():
            if val > k:
                res.append(key)
            else:
                continue
        return res