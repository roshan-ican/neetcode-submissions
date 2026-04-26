class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMin(nums) {

        let res = nums[0]
        for(let i =0; i< nums.length; i++){
             res = Math.min(res, nums[i])
        }
        return res

    }
}
