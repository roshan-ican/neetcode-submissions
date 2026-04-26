class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixProd = [1] * n
        prefixProd[0] = nums[0]
        
        for i in range(1, n):
            prefixProd[i] = prefixProd[i - 1] * nums[i]
        
        suffixProd = [1] * n
        suffixProd[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffixProd[i] = suffixProd[i + 1] * nums[i]
            
        res = [1] * n
        for i in range(n):
            left = prefixProd[i - 1] if i > 0 else 1
            right = suffixProd[i + 1] if i < n - 1 else 1
            res[i] = left * right
        return res