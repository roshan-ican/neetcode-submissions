class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let hashMap = new Map()
        // create a hash map
        // get count of the objects
        //  count is more than two 
        // return true
       for(let i = 0; i < nums.length; i++){
        if(hashMap.has(nums[i])){
                return true
            }
            hashMap.set(nums[i], 1)
       }
       return false
    }
}
