class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Dictionary to count frequency of each number
        count = {}
        
        # Bucket array: index = frequency, value = list of numbers with that frequency
        # Size is len(nums)+1 because max frequency can be len(nums)
        freq = [[] for i in range(len(nums) + 1)]

        # Count frequency of each number
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # Put numbers into buckets based on their frequency
        # n = number, c = count/frequency
        for n, c in count.items():
            freq[c].append(n)  # Add number to bucket at index = its frequency

        res = []
        # Start from highest frequency bucket and work backwards
        for i in range(len(freq) - 1, 0, -1):
            # Get all numbers from current frequency bucket
            for n in freq[i]:
                res.append(n)
                # Return once we have k most frequent numbers
                if len(res) == k:
                    return res
