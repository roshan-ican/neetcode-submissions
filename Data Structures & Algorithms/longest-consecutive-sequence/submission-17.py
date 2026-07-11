class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        our_set = set(nums)
        max_length = 0
   
        for num in our_set:

            if num - 1 not in our_set:
                next_num = num + 1

                while next_num in our_set:
                    next_num = next_num + 1

                curr_streak = next_num - num
                max_length = max(max_length, curr_streak)
                 
        return max_length

