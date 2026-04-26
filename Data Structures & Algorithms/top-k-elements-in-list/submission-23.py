class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for key, val in count.items():
            freq[val].append(key)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res








        # count_map = {}
        # res = []
        # for n in nums:
        #     if n in count_map:
        #         count_map[n] += 1
        #     else:
        #         count_map[n] = 1

        # arr = sorted(count_map.items(), key = lambda x : x[1], reverse=True)

        # for key,v in arr:
        #     if len(res) >= k:
        #         break
        #     res.append(key)
        # return res

        