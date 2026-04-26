class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count_map = {}
        res = []
        for n in nums:
            if n in count_map:
                count_map[n] += 1
            else:
                count_map[n] = 1

        arr = sorted(count_map.items(), key = lambda x : x[1], reverse=True)

        for key,v in arr:
            if len(res) >= k:
                break
            res.append(key)
        return res

        