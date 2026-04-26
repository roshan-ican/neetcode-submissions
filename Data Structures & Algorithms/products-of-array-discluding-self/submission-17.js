class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {

        let n = nums.length;
        let net = Array(n).fill(1)

        let runP = 1
        for(let i = 0; i<n;i++){
            net[i] = runP
            runP *= nums[i]
        }
        runP = 1
        for(let i = n-1; i >= 0; i--){
            net[i] *= runP
            runP *= nums[i]
        }
        return net
    }
}
