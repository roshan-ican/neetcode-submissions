class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    majorityElement(nums) {
        let majority = {}
        let n = nums.length
        let times = Math.floor(n / 3)
        let result = []

        for(let i = 0; i < n; i++){
            if(nums[i] in majority){
                majority[nums[i]] += 1
            } else{
                majority[nums[i]] = 1
            }
        }
        for(const [key, value] of Object.entries(majority)){
            if(value > times){
                result.push(Number(key))
            }
        }
        return result
    }
}
