class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i -1]:
                continue
            start = i + 1
            end = len(nums) - 1
            while start < end:
                triplet = nums[i] + nums[start] + nums[end]
                if(triplet == 0):
                    result.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1
                        
                elif triplet < 0:
                    start+=1
                else:
                    end -= 1
                
            
        return result