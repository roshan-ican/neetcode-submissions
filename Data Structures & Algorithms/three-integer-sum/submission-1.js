class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
    nums.sort((a, b) => a - b); // Sort the array to handle duplicates easily
    const target = 0;
    const results = [];

    for (let i = 0; i < nums.length - 2; i++) {
        // Skip duplicates for the first number
        if (i > 0 && nums[i] === nums[i - 1]) continue;

        let left = i + 1, right = nums.length - 1;

        while (left < right) {
            const sum = nums[i] + nums[left] + nums[right];
            if (sum === target) {
                results.push([nums[i], nums[left], nums[right]]);

                // Skip duplicates for the second number
                while (left < right && nums[left] === nums[left + 1]) left++;
                // Skip duplicates for the third number
                while (left < right && nums[right] === nums[right - 1]) right--;

                left++;
                right--;
            } else if (sum < target) {
                left++;
            } else {
                right--;
            }
        }
    }

    return results;
    }
}
