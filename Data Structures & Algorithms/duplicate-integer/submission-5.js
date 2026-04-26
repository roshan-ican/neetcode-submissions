class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
    let dups = nums.some((val,i ) => nums.indexOf(val) !== i)
    return dups
    }
}
