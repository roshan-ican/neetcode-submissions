class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[]
        step = 1
        n = len(nums)
        for i in range(n):
            prefix.append(step)
            step *= nums[i] 
        suffix = [1] * n
        step = 1
        for j in range(n - 1, -1, -1):
            suffix[j] = step
            step *= nums[j]
        result = [p * s for p,s in zip(prefix, suffix)]
        return result
        