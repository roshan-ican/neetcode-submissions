class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number}
     */
    maxFrequency(nums, k) {

        nums.sort((a, b) => a - b)
        let total = 0
        let res = 0
        let l = 0
        let r = 0
        while(r < nums.length){
            total+=nums[r]
            while(nums[r] * (r - l + 1) > total + k){
                total-=nums[l]
                l += 1
            }
        res = Math.max(res, r - l + 1)
        r += 1

        }
        return res
    }
}
