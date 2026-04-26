class Solution:
    def trap(self, height: List[int]) -> int:
        # so we are having like each line and next 
        # if there is gap we need to use formula -> min(height[i], height[r]) - heght[i]

        # we need to keep moving and adding to our maxWater

        l = 0
        r = len(height) - 1
        leftMax, rightMax = height[l],height[r]
        maxWater = 0

        while l < r:
            if leftMax < rightMax:
                l+=1
                leftMax = max(leftMax, height[l])
                maxWater += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                maxWater += rightMax - height[r]

        return maxWater