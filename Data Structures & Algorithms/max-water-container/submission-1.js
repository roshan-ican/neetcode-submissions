class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let maxWater = 0
        let left = 0
        let right = heights.length-1

        while(left < right){
            let w = right - left
            let h = Math.min(heights[left], heights[right])
            let currWater = w * h
            maxWater = Math.max(maxWater, currWater)

            if(heights[left] < heights[right]){
                left++
            } else {
                right--
            }
        }
        return maxWater
    }
}
