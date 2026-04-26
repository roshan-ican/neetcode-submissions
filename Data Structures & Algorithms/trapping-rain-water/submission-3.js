class Solution {
    /**
     * @param {number[]} height
     * @return {number}
     */
    trap(height) {
        let n = height.length
        let l = 0
        let r = n - 1
        let res = 0
        let leftMax = 0, rightMax = 0;


        while(l < r){
            if(height[l] < height[r]){
                leftMax = Math.max(leftMax, height[l])
                res += leftMax - height[l]
                l++
            } else{
                rightMax = Math.max(rightMax, height[r])
                res += rightMax - height[r]
                r--
            }
        }
        console.log(res, "__res__")
        return res
    }
}
