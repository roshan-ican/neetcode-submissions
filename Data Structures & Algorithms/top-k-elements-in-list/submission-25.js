class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {

        const count = {}
        for(let n of nums){
            if(n in count){
                count[n] += 1
            }else{
                count[n] = 1
            }
        }
        const arr = Object.entries(count)
        arr.sort((a,b) => b[1] - a[1])
        const res = []
        for(let i = 0; i < k; i++){
            res.push(arr[i][0])
        }
        return res
    }
}
