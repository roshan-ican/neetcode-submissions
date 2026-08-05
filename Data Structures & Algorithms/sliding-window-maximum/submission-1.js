class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    maxSlidingWindow(nums, k) {
        // move with k and take max
        let res = []
        // slice the block
        for (let i = 0; i + k <= nums.length; i++) {
            let block = nums.slice(i, i + k)
            res.push(Math.max(...block))
        }

        console.log(res, "_res")
        return res
    }
}
