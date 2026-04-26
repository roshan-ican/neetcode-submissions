class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const map = {}

        for(let n of nums){
            if(n in map){
                map[n] += 1
            } else{
                map[n] = 1
            }
        }
        for(const value of Object.values(map)){
            if(value > 1){
                return true
            }
        }
        return false

    }
}
