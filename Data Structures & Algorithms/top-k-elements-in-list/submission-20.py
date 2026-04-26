class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count_map = {}

        for i, n in enumerate(nums):
            if n in count_map:
                count_map[n] += 1
            else:
                count_map[n] = 1

        # Sort by frequency (value) in descending order
        arr = sorted(count_map.items(), key=lambda x: x[1], reverse=True)

        # Take top k frequent elements
        for key, val in arr:
            if len(res) >= k:
                break
            res.append(key)

        return res

        