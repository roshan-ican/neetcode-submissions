class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        l = 0
        r = n - 1
        pos = n - 1
        
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res[pos] = nums[l] * nums[l]
                l+=1
            else:
                res[pos] = nums[r] * nums[r]
                r -= 1
            pos-= 1
        return res





        
        # for j in range(len(arr)):
        #     if arr[i] > arr[j]:
        #         arr[j], arr[i] = arr[i], arr[j]
        #         i+=1
        #     else:
        #         arr[i], arr[j] = arr[j], arr[i]
        #         i+=1
        # print(arr,'dsflsdk')
