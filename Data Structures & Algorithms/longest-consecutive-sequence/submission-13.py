class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums)== 0): return 0
        arr = sorted(set(nums))
        count = 1
        max_count = 1
        
        for i in range(len(arr) - 1):
            if abs(arr[i] - arr[i + 1]) == 1:
                count+=1
                max_count = max(max_count, count)
            else:
                count = 1
        return max_count