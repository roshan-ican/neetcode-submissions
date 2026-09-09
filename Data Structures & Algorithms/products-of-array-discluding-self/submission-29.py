class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prod_pref = [1] * len(nums)
        prod_sufx = [1] * len(nums)

        for i in range(1, len(nums)):
            prod_pref[i] = prod_pref[i - 1] * nums[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            prod_sufx[i] = prod_sufx[i + 1] * nums[i + 1]

        # print(prod_pref, prod_sufx)
        result = []
        for i in range(len(prod_pref)):
            result.append(prod_pref[i] * prod_sufx[i])
        return result