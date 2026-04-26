class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
        nums.sort((a,b) => a - b)

        let result = []

        for(let i = 0; i < nums.length; i++){
            if (i > 0 && nums[i] === nums[i - 1]) continue
            let left = i + 1
            let right = nums.length - 1
            while(left < right){
            const pair = nums[i] + nums[left] + nums[right]
                if(pair === 0){
                    result.push([nums[i], nums[left], nums[right]])
                    left++
                    right--
                    while (left < right && nums[left] === nums[left - 1]) left++
                    while (left < right && nums[right] === nums[right + 1]) right--
                } else if(pair < 0){
                    left++
                }else{
                    right--
                }
            }
        }
        console.log(result, "__result_")
        return result
        
    
    }
}
