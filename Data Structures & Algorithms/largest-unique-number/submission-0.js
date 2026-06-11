class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    largestUniqueNumber(nums) {
        let counts = {}

        for(let i =0; i< nums.length; i++){
            if(counts[nums[i]] === undefined){
                counts[nums[i]] = 1
            } else{
                counts[nums[i]] += 1
            }
        }
        let maxUnique = -1

        for(let key in counts){
            let currNum = Number(key)

            if(counts[key] === 1 && currNum > maxUnique){
                maxUnique = currNum
            }
        }
     return maxUnique
    }
}
