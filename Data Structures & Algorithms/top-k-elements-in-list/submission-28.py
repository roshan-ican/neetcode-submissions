import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count the most freq elements with a map
        hash_map = {}
        for n in nums:
            if n in hash_map:
                hash_map[n] += 1
            else:
                hash_map[n] = 1
        heap = []
        for num, freq in hash_map.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        print(heap, "ajdsklf")
        result = []
        for freq, num in heap:

            result.append(num)

        return result
                        

