class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        // low and high and mid
        let low = 0, high = nums.length - 1

   
        while(low <= high){
            let mid = Math.round((low + high)/2)
            if(target < nums[mid]){
                high = mid - 1

            }else if(target > nums[mid]){
                low = mid + 1
            }else{
                return mid
            }
        }
        return -1
    }
}
