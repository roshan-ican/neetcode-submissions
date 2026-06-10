class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        const numSets = new Set(nums)
        let long = 0;

        for(let n of numSets){
            if(!numSets.has(n - 1)){
                let length = 1
                while(numSets.has(n + length)){
                    length++
                }
                long = Math.max(long, length)
            }
        }
        return long
    }
}


