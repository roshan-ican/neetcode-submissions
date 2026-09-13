class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # res = []
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):
        #             add = nums[i] + nums[j] + nums[k]
        #             triplet = sorted([nums[i], nums[j], nums[k]])
        #             if add == 0 and triplet not in res:
        #                 res.append(triplet)
        # return res
        nums.sort()
        i = 0
        res = []
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1
            while j < k:
                add = nums[i] + nums[j] + nums[k]
                triplet = [nums[i], nums[j], nums[k]]
                if add == 0 and triplet not in res:
                    res.append(triplet)
                    j+=1
                    k-=1             
                elif add < 0:
                    j += 1
                else:
                    k -= 1
            i+=1
        return res

