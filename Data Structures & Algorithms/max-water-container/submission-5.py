class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        max = 0
        while start != end:
            area = (end - start) * min(heights[start], heights[end])
            if area > max:
                max = area
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
        return max