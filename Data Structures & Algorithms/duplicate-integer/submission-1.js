class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        // let count = 0
        const frequencies = {}
        for(let item of nums){
            frequencies[item] = (frequencies[item] || 0) + 1;
        }
        console.log(frequencies, "frequencies")
        const arr = Object.values(frequencies)
        console.log(arr, "non_arr")
        for(let count of arr){
           if(count > 1){
            return true
           }
        }
        return false

    }
}
