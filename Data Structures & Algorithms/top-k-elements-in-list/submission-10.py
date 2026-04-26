class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        n = len(nums)
        bucket = [[] for _ in range(n+1)]

        for i in range(n):
            val = nums[i]
            count[val] = 1 + count.get(val, 0)
        for n, c in count.items():
            bucket[c].append(n)
        res = []
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if(len(res) == k):
                    return res
        