class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
  
        maxSum =nums[0]
        currSum = nums[0]

        for r in range(1, len(nums)):
            if nums[r] > nums[r-1]:
                currSum += nums[r]
                print(currSum, "first_sum")
            else:
                currSum = nums[r] # resetting
                print(currSum, "second_sum")
            maxSum= max(maxSum, currSum)
        return maxSum

        