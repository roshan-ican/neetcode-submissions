class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        buckets = [[] for _ in range(len(nums) + 1)]

        for i, n in enumerate(nums):
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
   
        for key, value in freq.items():
            if 0 <= value <= len(buckets):
                buckets[value].append(key)
        res = []
        for index, sub_array in reversed(list(enumerate(buckets))):
            for num in sub_array:
                res.append(num)
                if len(res) == k:
                    return res
        return res


        # mapping