class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        # get avg
        # check in window
        # keep a cout on great than thresholds
        window = sum(arr[:k])
        count = 0

        if window >= threshold * k:
            count+=1

        for i in range(k, len(arr)):
            window = window - arr[i - k] + arr[i]
            if window >= threshold * k:
                count+=1
        return count
