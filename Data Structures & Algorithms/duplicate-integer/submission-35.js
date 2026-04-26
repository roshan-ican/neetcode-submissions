class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const hash_map = {}

        for(let n of nums){
            if(n in hash_map){
                hash_map[n] += 1
            } else{
                hash_map[n] = 1
            }
        }
        console.log(hash_map, "__v__")
        for(let v of Object.values(hash_map)){
            if(v > 1){
                return true
            }
        }
        return false
        
    }
}
