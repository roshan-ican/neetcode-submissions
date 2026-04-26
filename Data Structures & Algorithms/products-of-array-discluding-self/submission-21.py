class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # we start from index of 1
        # we have a l pointer
        # as we move we multiply
        # and we add it and we move our pointer
        n= len(nums)
        newArr = [1] * n 
        l = 1
        for i in range(n):
            newArr[i] = l
            # if currM > mx:
            l *= nums[i]
            # newArr.append(mx)
        
        r = 1
        for i in range(n -1, -1, -1):
            newArr[i] *= r
            r *= nums[i]

        return newArr
        # prd = 1
        # for i in range(len(nums)):
        #     prd *= nums[i]
        # res = [1] * len(nums)
        # for i in range(len(nums)):
        #     res[i] = int(prd / nums[i])
        # return res



