class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findDuplicate(nums) {
        let chars = {}
        let mostCount = 0
        for(let i =0 ; i < nums.length; i++){
            if(nums[i] in chars){
                chars[nums[i]] += 1
            } else{
                chars[nums[i]] = 1
            }
        }

        for(const [key, value] of Object.entries(chars)){
            let curr = value
            if(curr > 2){
                mostCount = key
            }
            else if(curr > mostCount) {
                mostCount = key
            }
        }
        return mostCount
    }
}
