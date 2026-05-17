class Solution {
    /**
     * @param {number[]} nums1
     * @param {number[]} nums2
     * @return {number[]}
     */
    anagramMappings(nums1, nums2) {
        // first we need to get the index of the first arr
        const valToIndices = new Map()

        for(let i = 0; i < nums2.length; i++){
            const val = nums2[i]
            if(!valToIndices.has(val)){
                valToIndices.set(val, [])
            }
            valToIndices.get(val).push(i)
        }
        const mapping = new Array(nums1.length);
        for(let i = 0; i < nums1.length; i++){
            const val = nums1[i]
            mapping[i] = valToIndices.get(val).shift()
        }
        return mapping
        
    }
}
