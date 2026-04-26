class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    // topKFrequent(nums, k) {
    //     // count the occurances
    //     // keep the key and value
    //     // if the count's obj value is greater than 1
    //     // and take k as count and return the higehest count
    //     const frequencies = {};
    //     for(let item of nums){
    //         if(frequencies[item]){
    //             frequencies[item]++
    //         }else{
    //             frequencies[item]= 1
    //         }
    //     }
    //     console.log(frequencies, "frequencies")
    //     const arr = Object.keys(frequencies)
    //     console.log(arr.length, "___arr___", arr)
    //     if(arr.length === 1){
    //         return arr
    //     }
    
    // }
    // getMaxKElements(arr, k) {
    //     console.log(arr, "inside_getMaxKElements")
    //     if (k > arr.length) return arr;
    //     const result =  arr.sort((a, b) => b - a).slice(0, k);
    //     console.log(result, "result___")
    //     return result
    // }
    topKFrequent(nums, k) {
        const frequencies = {};
        for(let item of nums){
            if(frequencies[item]){
                frequencies[item]++
            }else{
                frequencies[item]= 1
            }
        }
        const sortedKeys = Object.keys(frequencies).sort((a, b) => frequencies[b] - frequencies[a]);
        console.log(sortedKeys, "sortedKeys")
        return sortedKeys.slice(0, k).map(Number);
        
    
    }
}
