class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        max_area = 0

        for r in range(len(heights)):
            current = heights[r]
            while stack and current < heights[stack[-1]]:
                p_idx = stack.pop()
                height = heights[p_idx] 

                if stack:
                    width = r - stack[-1] - 1
                else:
                    width = r
                
                area = height * width
                max_area = max(max_area, area)
            stack.append(r)
        heights.pop()
        return max_area
    
        