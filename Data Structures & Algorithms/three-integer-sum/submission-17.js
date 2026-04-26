class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
 threeSum(nums) {
    const results = [];
    if (!nums || nums.length < 3) return results; // ✅ Proper edge case
    nums.sort((a, b) => a - b);

    for (let i = 0; i < nums.length - 2; i++) {
        if (i > 0 && nums[i] === nums[i-1]) continue; // ✅ Skip duplicates

        let left = i + 1;
        let right = nums.length - 1;

        while (left < right) {
            const sum = nums[i] + nums[left] + nums[right];
            
            if (sum === 0) {
                results.push([nums[i], nums[left], nums[right]]); // ✅ Correct output
                // Skip duplicates for left/right
                while (left < right && nums[left] === nums[left+1]) left++;
                while (left < right && nums[right] === nums[right-1]) right--;
                left++;
                right--;
            } else if (sum < 0) {
                left++;
            } else {
                right--;
            }
        }
    }
    return results;
}

}
