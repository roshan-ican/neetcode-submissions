class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
    const count = new Map()
    for(let i of nums){
        if(count.has(i)) return true
        count.set(i,1)
    }
    return false
    }
}
