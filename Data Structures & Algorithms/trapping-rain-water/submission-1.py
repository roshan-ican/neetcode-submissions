class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]

        water = 0
        for i in range(len(height) - 1):
            trapped = min(l, r) - height[i]

            if height[l] < height[r]:
                l += 1
                left_max = max(left_max, height[l])
                water += max(0, left_max- height[l])
            else:
                r -= 1
                right_max = max(right_max, height[r])
                water += max(0, right_max- height[r])
        return water