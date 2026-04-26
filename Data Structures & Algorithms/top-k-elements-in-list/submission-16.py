import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # hash map
        my_map = {}
        for n in nums:
            if n not in my_map:
                my_map[n] = 1
            else:
                my_map[n] += 1
        result = heapq.nlargest(k, my_map.keys(), key=my_map.get)
        return result
            


