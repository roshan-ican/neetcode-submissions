class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequencies using Counter (or manual dict if you prefer)
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        print(count, "kkkddd")
        # Use heapq.nlargest to get k elements with highest frequency
        return self.get_top_k(count, k)

    @staticmethod
    def get_top_k(count: dict, k: int) -> List[int]:
        # Return k keys with highest frequency
        return heapq.nlargest(k, count.keys(), key=count.get)