class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {

        const n = nums.length;
        const result = new Array(nums).fill(1);
        
        let leftProduct = 1;
        for (let i = 0; i < n; i++) {
            result[i] = leftProduct;  // Store left product
            leftProduct *= nums[i];   // Update for next iteration
        }
        
        let rightProduct = 1
        for(let i=n-1; i >= 0; i--){
            result[i] *= rightProduct
            rightProduct *= nums[i] 
        }
        return result
    }
}
